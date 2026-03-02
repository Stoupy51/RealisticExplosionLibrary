
# Imports
import os

from beet import BlockTag, Context
from beet.core.utils import JsonDict
from stewbeet import *  # type: ignore

# Constants
BLAST_RESISTANCE_BLOCKS_FILE: str = "src/blast_resistance_blocks.txt"
GENERATED_SUMMONS_FOLDER: str = "generated_summons"
FALLING_BLOCK_FOLDER: str = "falling_block"
EXPLOSION_FOLDER: str = "explosion"

# URLs to fetch the list of items and blocks from the Minecraft registry (based on 1.21)
ITEM_TXT: str = "https://raw.githubusercontent.com/PixiGeko/Minecraft-generated-data/master/1.21/releases/1.21.11/custom-generated/registries/item.txt"
BLOCK_TXT: str = "https://raw.githubusercontent.com/PixiGeko/Minecraft-generated-data/master/1.21/releases/1.21.11/custom-generated/registries/block.txt"

@stp.simple_cache()
def fetch_url(url: str) -> list[str]:
    """Fetch a text file from a URL and return its content as a list of lines."""
    import requests

    with requests.get(url) as response:
        return response.text.splitlines()

def get_list_from_items_and_blocks(ctx: Context) -> list[str]:
    """ Return a list of items that are also blocks. """
    # Fallback: use a comprehensive list based on Minecraft 1.21
    # This is more reliable than trying to parse vanilla data structures
    # We'll fetch from the registry files that beet might have cached
    items_list = fetch_url(ITEM_TXT)
    blocks_list = fetch_url(BLOCK_TXT)

    # For each item, add it to the final list if it's in the block list
    final_list: list[str] = []
    for item in items_list:
        if item in blocks_list:
            final_list.append(item)

    # Return the final list
    return final_list


def generate_explodable_blocks_tags(ctx: Context, ns: str) -> None:
    """Generate the list of blocks that can be destroyed by the explosion by steps."""

    # Get vanilla blocks using beet's vanilla system or from URL
    blocks = fetch_url(BLOCK_TXT)

    # Read the blast resistance file
    blast_resistance_dict: dict[str, int] = {}
    blast_file_path = os.path.join(os.getcwd(), BLAST_RESISTANCE_BLOCKS_FILE)
    with open(blast_file_path) as file:
        for line in file.read().splitlines():
            line = line.split("\t")
            blast_resistance_dict[line[0]] = int(line[1])

    # Create a list of every blocks that have no blast resistance
    blocks_no_blast_resistance: list[str] = []
    for block in blocks:
        if block not in blast_resistance_dict:
            blocks_no_blast_resistance.append(block)

    ## Generate 4 tags: no_blast_resistance, equal_and_below_1200, equal_and_below_3600000, all

    # Tag 1: no_blast_resistance.json
    values: list[JsonDict] = [{"required": False, "id": block} for block in blocks_no_blast_resistance]
    ctx.data[ns].block_tags["no_blast_resistance"] = set_json_encoder(BlockTag({"values": values}))

    # Tag 2: equal_and_below_1200.json
    current_block_list: list[str] = []
    for block in blast_resistance_dict.keys():
        if blast_resistance_dict[block] <= 1200:
            current_block_list.append(block)
    values = [{"required": False, "id": f"#{ns}:no_blast_resistance"}]
    values.extend([{"required": False, "id": block} for block in current_block_list])
    ctx.data[ns].block_tags["equal_and_below_1200"] = set_json_encoder(BlockTag({"values": values}))

    # Tag 3: equal_and_below_3600000.json
    current_block_list = []
    for block in blast_resistance_dict.keys():
        if blast_resistance_dict[block] > 1200 and blast_resistance_dict[block] <= 3600000:
            current_block_list.append(block)
    values = [{"required": False, "id": f"#{ns}:equal_and_below_1200"}]
    values.extend([{"required": False, "id": block} for block in current_block_list])
    ctx.data[ns].block_tags["equal_and_below_3600000"] = set_json_encoder(BlockTag({"values": values}))

    # Tag 4: all.json
    current_block_list = []
    for block in blast_resistance_dict.keys():
        if blast_resistance_dict[block] > 3600000:
            current_block_list.append(block)
    values = [{"required": False, "id": f"#{ns}:equal_and_below_3600000"}]
    values.extend([{"required": False, "id": block} for block in current_block_list])
    ctx.data[ns].block_tags["all"] = set_json_encoder(BlockTag({"values": values}))


def generate_summons_files(ctx: Context, ns: str) -> None:
    """Generate the .mcfunction files that will handle which falling block will be summoned."""

    # Get the list of items that are also blocks
    items: list[str] = [*get_list_from_items_and_blocks(ctx), "minecraft:fire", "minecraft:lava", "minecraft:water"]  # Special blocks just in case

    # Create dictionaries to group items by name length
    item_name_length_dict: dict[int, list[str]] = {}
    for item in items:
        item_name_length = len(item)

        if item_name_length not in item_name_length_dict:
            item_name_length_dict[item_name_length] = []

        item_name_length_dict[item_name_length].append(item)

    # For each length, create a function file
    for item_name_length, items_list in item_name_length_dict.items():
        content = ""
        for item in items_list:
            content += f'execute if data storage {ns}:main {{id:"{item}"}} run summon falling_block ~ ~ ~ {{Tags:["realistic_explosion.new"],DropItem:0b,BlockState:{{Name:"{item}"}}}}\n'

        write_function(f"{ns}:{GENERATED_SUMMONS_FOLDER}/{item_name_length}", content)

    # Sort the list of item name lengths
    length_list = sorted(item_name_length_dict.keys())

    # Create the on_item function
    on_item_content = f"""
#> {ns}:{GENERATED_SUMMONS_FOLDER}/on_item
#
# @within			{ns}:{EXPLOSION_FOLDER}/main
# @executed			as & at the item entity from the explosion
#
# @input score		#falling_fire {ns}.data : indicates if the explosion should spawn falling block "fire"
# @output storage	{ns}:main Rotation : the rotation looking at the origin of the explosion
#
# @description		Calculate the length of the item name and execute the corresponding function
#
# @warning			This file is auto-generated, do not edit it manually!
#

# Copy the item id to the storage
data modify storage {ns}:main id set from entity @s Item.id

# If the falling block should be fire, set the id to "minecraft:fire"
execute if score #falling_fire {ns}.data matches 1 run data modify storage {ns}:main id set value "minecraft:fire"

# Get the length of the item name
execute store result score #length {ns}.data run data get storage {ns}:main id

# Execute the function that will summon the falling block
"""

    for item_name_length in length_list:
        on_item_content += f"execute if score #length {ns}.data matches {item_name_length} run function {ns}:{GENERATED_SUMMONS_FOLDER}/{item_name_length}\n"

    on_item_content += f"""
# Get rotation looking at the origin of the explosion and kill the item entity
execute at @s run tp @s ~ ~10 ~ facing entity @e[type=marker,tag=realistic_explosion.origin,limit=1] feet
execute at @s run tp @s ~ ~-10 ~

# Copy the rotation to the falling block and kill the item entity
data modify entity @e[type=falling_block,tag=realistic_explosion.new,sort=nearest,distance=..1,limit=1] Rotation set from entity @s Rotation
kill @s

# Schedule the function that applies the explosion motion
schedule function {ns}:{FALLING_BLOCK_FOLDER}/apply_motion_to_all 2t

"""

    write_function(f"{ns}:{GENERATED_SUMMONS_FOLDER}/on_item", on_item_content)


def generate_falling_block_folder(ctx: Context, ns: str) -> None:
    """Generate the .mcfunction files that will handle the falling block."""

    # apply_motion_to_all.mcfunction
    apply_motion_content = f"""
#> {ns}:{FALLING_BLOCK_FOLDER}/apply_motion_to_all
#
# @within			{ns}:{FALLING_BLOCK_FOLDER}
# @executed			default context
#
# @description		Apply the explosion motion to all falling blocks
#
# @warning			This file is auto-generated, do not edit it manually!
#

# Execute the function as all falling blocks to apply the explosion motion
execute as @e[type=falling_block,tag=realistic_explosion.new] at @s run function {ns}:{FALLING_BLOCK_FOLDER}/main

"""
    write_function(f"{ns}:{FALLING_BLOCK_FOLDER}/apply_motion_to_all", apply_motion_content)

    # main.mcfunction
    main_content = f"""
#> {ns}:{FALLING_BLOCK_FOLDER}/main
#
# @within			{ns}:{GENERATED_SUMMONS_FOLDER}/on_item
# @executed			as & at the new falling block
#
# @out storage	{ns}:main Rotation : the rotation looking at the origin of the explosion
# @output storage	{ns}:main Motion : the motion of the entity
#
# @description		Push away the falling block from the explosion origin
#
# @warning			This file is auto-generated, do not edit it manually!
#

# Get the rotation looking at the origin of the explosion
data modify storage {ns}:main Rotation set from entity @s Rotation

## Launch the entity
# Get the motion of the entity by summoning a temporary marker
execute positioned 0 0 0 summon marker run function {ns}:{FALLING_BLOCK_FOLDER}/get_motion_from_rotation

# Apply the motion to the entity
execute store result entity @s Motion[0] double 0.01 run data get storage {ns}:main Motion[0]
execute store result entity @s Motion[1] double 0.01 run data get storage {ns}:main Motion[1]
execute store result entity @s Motion[2] double 0.01 run data get storage {ns}:main Motion[2]

# Make clients update the entity nbt
data modify entity @s Glowing set value 1b
data modify entity @s Glowing set value 0b

# Remove the new tag from the entity
tag @s remove realistic_explosion.new

"""
    write_function(f"{ns}:{FALLING_BLOCK_FOLDER}/main", main_content)

    # get_motion_from_rotation.mcfunction
    get_motion_content = f"""
#> {ns}:{FALLING_BLOCK_FOLDER}/get_motion_from_rotation
#
# @within			{ns}:{FALLING_BLOCK_FOLDER}/main
# @executed			as the temporary marker & at the new falling block
#
# @input storage	{ns}:main Rotation : the rotation looking at the origin of the explosion
# @output storage	{ns}:main Motion : the motion of the entity
#
# @description		Fills the storage with the motion of the entity
#
# @warning			This file is auto-generated, do not edit it manually!
#

# Get the rotation of the entity
data modify entity @s Rotation set from storage {ns}:main Rotation

# Go backward (not forward because the rotation aim at the origin of the explosion)
execute at @s run tp @s ^ ^ ^-100

# Get the position of the entity into the storage
data modify storage {ns}:main Motion set from entity @s Pos

# Kill the entity
kill @s

"""
    write_function(f"{ns}:{FALLING_BLOCK_FOLDER}/get_motion_from_rotation", get_motion_content)


def generate_explosion_manager(ctx: Context, ns: str) -> None:
    """Generate the .mcfunction files that will handle the explosion."""

    # explode.mcfunction (entry point)
    explode_content = f"""
#> {ns}:explode
#
# @within			Nothing, this function is manually called by the Library's User
# @executed			as unknown entity & at the explosion origin
#
# @input score		#explosion_power {ns}.data : the power of the explosion
# @input score		#falling_fire {ns}.data : indicates if the explosion should spawn falling block "fire" (default: 0)
#
# @description		Summons a temporary marker and execute the function that will handle the explosion
#
# @warning			This file is auto-generated, do not edit it manually!
#

# Create the scoreboard objective if it doesn't exist
scoreboard objectives add {ns}.data dummy

# Execute the function as the temporary marker
execute summon marker run function {ns}:{EXPLOSION_FOLDER}/main

"""
    write_function(f"{ns}:explode", explode_content)

    # explosion/main.mcfunction
    main_content = f"""
#> {ns}:{EXPLOSION_FOLDER}/main
#
# @within			{ns}:explode
# @executed			as the temporary marker & at the explosion origin
#
# @input score		#explosion_power {ns}.data : the power of the explosion
# @input score		#falling_fire {ns}.data : indicates if the explosion should spawn falling block "fire" (default: 0)
#
# @output score		#power_state {ns}.data : the power state of the explosion (0, 1, 2 or 3)
#
# @description		Execute the function that will handle the explosion
#
# @warning			This file is auto-generated, do not edit it manually!
#

# Add the tag to the marker for items to be able to detect position
tag @s add realistic_explosion.origin

# Add a tag to all current items to prevent them from being selected by the function
tag @e[type=item] add realistic_explosion.old

# Destroy the nearest 27 blocks without dropping anything
scoreboard players set #power_state {ns}.data 0
execute if score #explosion_power {ns}.data matches 1200.. run scoreboard players set #power_state {ns}.data 1
execute if score #explosion_power {ns}.data matches 3600000.. run scoreboard players set #power_state {ns}.data 2
execute if score #explosion_power {ns}.data matches 10000000.. run scoreboard players set #power_state {ns}.data 3
execute if score #power_state {ns}.data matches 0 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #{ns}:no_blast_resistance
execute if score #power_state {ns}.data matches 1 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #{ns}:equal_and_below_1200
execute if score #power_state {ns}.data matches 2 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #{ns}:equal_and_below_3600000
execute if score #power_state {ns}.data matches 3 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #{ns}:all

# For each 9 + 9 + 9 + 9 + 9 + 9 blocks stick-around the explosion origin, execute the function that will handle the block
"""

    # Generate the positioned commands for surrounding blocks
    for x in range(-2, 3, 1):
        for y in range(-2, 3, 1):
            for z in range(-2, 3, 1):
                # Ignore blocks too close to the explosion origin
                if abs(x) < 2 and abs(y) < 2 and abs(z) < 2:
                    continue

                # Ignore blocks not stick to the fill zone
                if (abs(x) + abs(y) + abs(z)) > 4 or (abs(x) + abs(y) == 4) or (abs(x) + abs(z) == 4) or (abs(y) + abs(z) == 4):
                    continue

                main_content += f"execute positioned ~{x} ~{y} ~{z} if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {{Fuse:10s}}\n"
                main_content += f"execute positioned ~{x} ~{y} ~{z} unless block ~ ~ ~ air run function {ns}:{EXPLOSION_FOLDER}/on_block\n"

    main_content += f"""
# For each item that is not tagged as "realistic_explosion.old", execute the function that will handle the item
execute as @e[type=item,tag=!realistic_explosion.old] at @s run function {ns}:{GENERATED_SUMMONS_FOLDER}/on_item

# Remove the tag from all items
tag @e[type=item,tag=realistic_explosion.old] remove realistic_explosion.old

# Kill the marker
kill @s

"""
    write_function(f"{ns}:{EXPLOSION_FOLDER}/main", main_content)

    # explosion/on_block.mcfunction
    on_block_content = f"""
#> {ns}:{EXPLOSION_FOLDER}/on_block
#
# @within			{ns}:{EXPLOSION_FOLDER}/main
# @executed			as the temporary marker & at a position of a block to destroy
#
# @input score		#power_state {ns}.data : the power state of the explosion (0, 1, 2 or 3)
#
# @description		Destroys the block if it can be destroyed by the explosion
#

# Depending on the power of the explosion, execute the correct setblock command
execute if score #power_state {ns}.data matches 0 if block ~ ~ ~ #{ns}:no_blast_resistance run setblock ~ ~ ~ air destroy
execute if score #power_state {ns}.data matches 1 if block ~ ~ ~ #{ns}:equal_and_below_1200 run setblock ~ ~ ~ air destroy
execute if score #power_state {ns}.data matches 2 if block ~ ~ ~ #{ns}:equal_and_below_3600000 run setblock ~ ~ ~ air destroy
execute if score #power_state {ns}.data matches 3 if block ~ ~ ~ #{ns}:all run setblock ~ ~ ~ air destroy

"""
    write_function(f"{ns}:{EXPLOSION_FOLDER}/on_block", on_block_content)


# Main entry point (ran just before finalizing the build process)
@stp.measure_time(printer=stp.info, message="Generated Realistic Explosion Library files")
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id

    # Generate all the explosion library files
    stp.info("Generating Realistic Explosion Library files...")

    generate_explodable_blocks_tags(ctx, ns)
    stp.info("  - Generated explodable blocks tags")

    generate_summons_files(ctx, ns)
    stp.info("  - Generated summon files")

    generate_falling_block_folder(ctx, ns)
    stp.info("  - Generated falling block functions")

    generate_explosion_manager(ctx, ns)
    stp.info("  - Generated explosion manager")

    pass


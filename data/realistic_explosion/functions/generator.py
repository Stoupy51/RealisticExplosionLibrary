
## Python function that aims to generate .mcfunction files that will handle which falling block will be summoned
## Items and Blocks are retrieved manually from: https://github.com/PixiGeko/Minecraft-generated-data/blob/master/1.20/releases/1.20.1/custom-generated/registries/item.txt

# Imports
import os

# Stop if the execution is not in the same folder as the script
if os.getcwd() != os.path.dirname(os.path.realpath(__file__)):
	print("Please execute this script in the same folder as the script")
	exit()

# Constants
BLAST_RESISTANCE_BLOCKS_FILE = "blast_resistance_blocks.txt"	# https://minecraft.fandom.com/wiki/Explosion#Blast_resistance
BLOCKS_TAG_PATH = "../tags/blocks"
GENERATED_SUMMONS_FOLDER = "generated_summons"
FALLING_BLOCK_FOLDER = "falling_block"
EXPLOSION_FOLDER = "explosion"

# Generate the list of blocks that can be destroyed by the explosion by steps
def generateExplodableBlocksTags() -> None:

	# Create the folder if it doesn't exist
	if not os.path.exists(BLOCKS_TAG_PATH):
		os.makedirs(BLOCKS_TAG_PATH)
	
	# Delete the content of the folder (ending with .json)
	for file in os.listdir(BLOCKS_TAG_PATH):
		if file.endswith(".json"):
			os.remove(f"{BLOCKS_TAG_PATH}/{file}")

	# Open the file with every blocks and read the content
	with open("block.txt", "r") as file:
		blocks = file.read().splitlines()
	
	# Open the file with every blast resistance blocks and read the content
	blast_resistance_dict = {}
	with open(BLAST_RESISTANCE_BLOCKS_FILE, "r") as file:
		for line in file.read().splitlines():
			line = line.split("\t")
			blast_resistance_dict[line[0]] = int(line[1])
	
	# Create a list of every blocks that have no blast resistance
	blocks_no_blast_resistance = []
	for block in blocks:
		if block not in blast_resistance_dict:
			blocks_no_blast_resistance.append(block)

	## Generate 4 tags : all blocks, blocks equal and below 3600000, blocks equal and below 1200
	# Create the file "all.json"
	with open(f"{BLOCKS_TAG_PATH}/all.json", "w") as file:
		blocks_beautify_json = "\",\n\t\t\"".join(blocks)
		file.write(f"""{{\n\t"values": [\n\t\t"{blocks_beautify_json}"\n\t]\n}}""")
	
	# Create the file "equal_and_below_3600000.json"
	with open(f"{BLOCKS_TAG_PATH}/equal_and_below_3600000.json", "w") as file:
		
		# Create a list of every blocks that have a blast resistance equal or below 3600000
		current_block_list = blocks_no_blast_resistance.copy()
		for block in blast_resistance_dict.keys():
			if blast_resistance_dict[block] <= 3600000:
				current_block_list.append(block)
		
		# Sort the list
		current_block_list = sorted(current_block_list)

		# Write the list in the file
		blocks_beautify_json = "\",\n\t\t\"".join(current_block_list)
		file.write(f"""{{\n\t"values": [\n\t\t"{blocks_beautify_json}"\n\t]\n}}""")
	
	# Create the file "equal_and_below_1200.json"
	with open(f"{BLOCKS_TAG_PATH}/equal_and_below_1200.json", "w") as file:
		
		# Create a list of every blocks that have a blast resistance equal or below 1200
		current_block_list = blocks_no_blast_resistance.copy()
		for block in blast_resistance_dict.keys():
			if blast_resistance_dict[block] <= 1200:
				current_block_list.append(block)
		
		# Sort the list
		current_block_list = sorted(current_block_list)

		# Write the list in the file
		blocks_beautify_json = "\",\n\t\t\"".join(current_block_list)
		file.write(f"""{{\n\t"values": [\n\t\t"{blocks_beautify_json}"\n\t]\n}}""")
	
	# Create the file "no_blast_resistance.json"
	with open(f"{BLOCKS_TAG_PATH}/no_blast_resistance.json", "w") as file:
		
		# Sort the list
		blocks_no_blast_resistance = sorted(blocks_no_blast_resistance)

		# Write the list in the file
		blocks_beautify_json = "\",\n\t\t\"".join(blocks_no_blast_resistance)
		file.write(f"""{{\n\t"values": [\n\t\t"{blocks_beautify_json}"\n\t]\n}}""")
	
	# Print done
	print("- Generated explodable blocks tags successfully")




# Return a list of items that are also blocks
def getListFromItemsAndBlock() -> list:
	
	# Open the file "item.txt" and "block.txt" and read the content
	with open("item.txt", "r") as file:
		items = file.read().splitlines()
	with open("block.txt", "r") as file:
		blocks = file.read().splitlines()
	
	# For each item, add it to the final list if it's in the block list
	final_list = []
	for item in items:
		if item in blocks:
			final_list.append(item)
	
	# Return the final list
	return final_list


# Generate the .mcfunction files that will handle which falling block will be summoned
def generateSummonsFiles() -> None:
	
	# Get the list of items that are also blocks
	items = getListFromItemsAndBlock()
	
	# Create the folder if it doesn't exist
	if not os.path.exists(GENERATED_SUMMONS_FOLDER):
		os.makedirs(GENERATED_SUMMONS_FOLDER)

	# Delete the content of the folder (ending with .mcfunction)
	for file in os.listdir(GENERATED_SUMMONS_FOLDER):
		if file.endswith(".mcfunction"):
			os.remove(f"{GENERATED_SUMMONS_FOLDER}/{file}")

	# For each item, create a file in the "generated_summons" folder
	item_name_length_dict = {}
	for item in items:
		
		# Count the number of letters in the item name
		item_name_length = len(item)
		
		# If the item name length is not already in the list, add it
		if item_name_length not in item_name_length_dict:
			item_name_length_dict[item_name_length] = 0
		
		# Increment the number of items with the same name length
		item_name_length_dict[item_name_length] += 1

		# Open the file where the command will be written
		with open(f"{GENERATED_SUMMONS_FOLDER}/{item_name_length}.mcfunction", "a") as file:
			
			# Write the command in the file
			file.write(f"execute if data storage realistic_explosion:main {{id:\"{item}\"}} run summon falling_block ~ ~ ~ {{Tags:[\"realistic_explosion.new\"],DropItem:0b,BlockState:{{Name:\"{item}\"}}}}\n")

	# Sort the list of item name length
	length_list = item_name_length_dict.keys()
	length_list = sorted(length_list)

	# Open the file where the command will be written
	with open(f"{GENERATED_SUMMONS_FOLDER}/all.mcfunction", "w") as file:

		file.write(f"""
#> realistic_explosion:{GENERATED_SUMMONS_FOLDER}/all
#
# @within			???
# @executed			as & at the item entity from the explosion
#
# @output storage	realistic_explosion:main Rotation : the rotation looking at the origin of the explosion
#
# @description		Calculate the length of the item name and execute the corresponding function
#
# @warning			This file is auto-generated by the generator.py script, do not edit it manually!
#

# Get the length of the item name
execute store result score #length realistic_explosion.data run data get entity @s Item.id

# Copy the item id to the storage
data modify storage realistic_explosion:main id set from entity @s Item.id

# Execute the function that will summon the falling block
""")

		# For each item name length, execute the corresponding function
		for item_name_length in length_list:
			file.write(f"execute if score #length realistic_explosion.data matches {item_name_length} run function realistic_explosion:{GENERATED_SUMMONS_FOLDER}/{item_name_length}\n")

		# Write the following lines
		file.write(f"""
# Get rotation looking at the origin of the explosion and kill the item entity
tp @s ~ ~ ~ facing entity @e[type=marker,tag=realistic_explosion.origin,limit=1] feet
data modify storage realistic_explosion:main Rotation set from entity @s Rotation
kill @s

# Execute the function as the new falling block
execute as @e[type=falling_block,tag=realistic_explosion.new] at @s run function realistic_explosion:{FALLING_BLOCK_FOLDER}/main

""")
	
	# Print done
	print("- Generated summons files successfully")


# Generate the .mcfunction files that will handle the falling block
def generateFallingBlockFolder() -> None:
	
	# Create the folder if it doesn't exist
	if not os.path.exists(FALLING_BLOCK_FOLDER):
		os.makedirs(FALLING_BLOCK_FOLDER)
	
	# Delete the content of the folder (ending with .mcfunction)
	for file in os.listdir(FALLING_BLOCK_FOLDER):
		if file.endswith(".mcfunction"):
			os.remove(f"{FALLING_BLOCK_FOLDER}/{file}")
	
	# Open the main file
	with open(f"{FALLING_BLOCK_FOLDER}/main.mcfunction", "w") as file:

		file.write(f"""
#> realistic_explosion:{FALLING_BLOCK_FOLDER}/main
#
# @within			realistic_explosion:{GENERATED_SUMMONS_FOLDER}/all
# @executed			as & at the new falling block
#
# @input storage	realistic_explosion:main Rotation : the rotation looking at the origin of the explosion
#
# @description		Push away the falling block from the explosion origin
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

## Launch the entity
# Get the motion of the entity by summoning a temporary marker
execute positioned 0 0 0 summon marker run function realistic_explosion:{FALLING_BLOCK_FOLDER}/get_motion_from_rotation

# Apply the motion to the entity
execute store result entity @s Motion[0] double 0.03 run data get storage realistic_explosion:main Motion[0]
execute store result entity @s Motion[1] double 0.03 run data get storage realistic_explosion:main Motion[1]
execute store result entity @s Motion[2] double 0.03 run data get storage realistic_explosion:main Motion[2]

""")
	
	# Open the get_motion_from_rotation file
	with open(f"{FALLING_BLOCK_FOLDER}/get_motion_from_rotation.mcfunction", "w") as file:
		
		file.write(f"""
#> realistic_explosion:{FALLING_BLOCK_FOLDER}/get_motion_from_rotation
#
# @within			realistic_explosion:{FALLING_BLOCK_FOLDER}/main
# @executed			as the temporary marker & at the new falling block
#
# @input storage	realistic_explosion:main Rotation : the rotation looking at the origin of the explosion
# @output storage	realistic_explosion:main Motion : the motion of the entity
#
# @description		Fills the storage with the motion of the entity
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

# Get the rotation of the entity
data modify entity @s Rotation set from storage realistic_explosion:main Rotation

# Go backward (not forward because the rotation aim at the origin of the explosion)
execute at @s run tp @s ^ ^ ^-100

# Get the position of the entity into the storage
data modify storage realistic_explosion:main Motion set from entity @s Pos

# Kill the entity
kill @s

""")

	# Print done
	print("- Generated falling block folder successfully")



# Generate the .mcfunction files that will handle the explosion
def generateExplosionManager() -> None:

	# Create the explode file
	with open(f"explode.mcfunction", "w") as file:

		file.write(f"""
#> realistic_explosion:explode
#
# @within			Nothing, this function is manually called by the Library's User
# @executed			as unknown entity & at the explosion origin
#
# @description		Summons a temporary marker and execute the function that will handle the explosion
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

# Execute the function as the temporary marker
execute summon marker run function realistic_explosion:{EXPLOSION_FOLDER}/main

""")
	
	# Create the folder if it doesn't exist
	if not os.path.exists(EXPLOSION_FOLDER):
		os.makedirs(EXPLOSION_FOLDER)
	
	# Delete the content of the folder (ending with .mcfunction)
	for file in os.listdir(EXPLOSION_FOLDER):
		if file.endswith(".mcfunction"):
			os.remove(f"{EXPLOSION_FOLDER}/{file}")

	# Open the main file
	with open(f"{EXPLOSION_FOLDER}/main.mcfunction", "w") as file:
		
		file.write(f"""
#> realistic_explosion:{EXPLOSION_FOLDER}/main
#
# @within			realistic_explosion:explode
# @executed			as the temporary marker & at the explosion origin
#
# @description		Execute the function that will handle the explosion
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

# Add the tag to the marker
tag @s add realistic_explosion.origin

# Add a tag to all current items to prevent them from being selected by the function
tag @e[type=item] add realistic_explosion.old

# Destroy the nearest 27 blocks without dropping anything
fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:explodable_blocks

""")









# Main function
if __name__ == "__main__":
	print("\nRunning the generator.py script...\n")

	generateExplodableBlocksTags()
	generateSummonsFiles()
	generateFallingBlockFolder()
	generateExplosionManager()

	print("\nEverything is done!\n")


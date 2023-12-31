
#> realistic_explosion:explosion/main
#
# @within			realistic_explosion:explode
# @executed			as the temporary marker & at the explosion origin
#
# @input score		#explosion_power realistic_explosion:data : the power of the explosion
# @input score		#falling_fire realistic_explosion.data : indicates if the explosion should spawn falling block "fire" (default: 0)
#
# @output score		#power_state realistic_explosion:data : the power state of the explosion (0, 1, 2 or 3)
#
# @description		Execute the function that will handle the explosion
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

# Add the tag to the marker for items to be able to detect position
tag @s add realistic_explosion.origin

# Add a tag to all current items to prevent them from being selected by the function
tag @e[type=item] add realistic_explosion.old

# Destroy the nearest 27 blocks without dropping anything
#fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:explodable_blocks
scoreboard players set #power_state realistic_explosion.data 0
execute if score #explosion_power realistic_explosion.data matches 1200.. run scoreboard players set #power_state realistic_explosion.data 1
execute if score #explosion_power realistic_explosion.data matches 3600000.. run scoreboard players set #power_state realistic_explosion.data 2
execute if score #explosion_power realistic_explosion.data matches 10000000.. run scoreboard players set #power_state realistic_explosion.data 3
execute if score #power_state realistic_explosion.data matches 0 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:no_blast_resistance
execute if score #power_state realistic_explosion.data matches 1 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:equal_and_below_1200
execute if score #power_state realistic_explosion.data matches 2 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:equal_and_below_3600000
execute if score #power_state realistic_explosion.data matches 3 run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:all

# For each 9 + 9 + 9 + 9 + 9 + 9 blocks stick-around the explosion origin, execute the function that will handle the block
execute positioned ~-2 ~-1 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~-1 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~-1 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~-1 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~-1 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~-1 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~0 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~0 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~0 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~0 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~0 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~0 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~1 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~1 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~1 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~1 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-2 ~1 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-2 ~1 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~-2 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~-2 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~-2 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~-2 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~-2 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~-2 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~-1 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~-1 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~-1 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~-1 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~0 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~0 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~0 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~0 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~1 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~1 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~1 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~1 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~2 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~2 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~2 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~2 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~-1 ~2 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~-1 ~2 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~-2 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~-2 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~-2 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~-2 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~-2 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~-2 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~-1 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~-1 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~-1 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~-1 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~0 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~0 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~0 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~0 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~1 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~1 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~1 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~1 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~2 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~2 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~2 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~2 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~0 ~2 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~0 ~2 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~-2 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~-2 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~-2 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~-2 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~-2 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~-2 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~-1 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~-1 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~-1 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~-1 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~0 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~0 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~0 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~0 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~1 ~-2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~1 ~-2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~1 ~2 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~1 ~2 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~2 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~2 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~2 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~2 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~1 ~2 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~1 ~2 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~-1 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~-1 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~-1 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~-1 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~-1 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~-1 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~0 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~0 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~0 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~0 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~0 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~0 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~1 ~-1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~1 ~-1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~1 ~0 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~1 ~0 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block
execute positioned ~2 ~1 ~1 if block ~ ~ ~ tnt run summon tnt ~ ~ ~ {Fuse:10s}
execute positioned ~2 ~1 ~1 unless block ~ ~ ~ air run function realistic_explosion:explosion/on_block

# For each item that is not tagged as "realistic_explosion.old", execute the function that will handle the item
execute as @e[type=item,tag=!realistic_explosion.old] at @s run function realistic_explosion:generated_summons/on_item

# Remove the tag from all items
tag @e[type=item,tag=realistic_explosion.old] remove realistic_explosion.old

# Kill the marker
kill @s


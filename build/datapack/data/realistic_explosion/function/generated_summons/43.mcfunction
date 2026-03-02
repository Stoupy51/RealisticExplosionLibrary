
#> realistic_explosion:generated_summons/43
#
# @executed	as @e[type=item,tag=!realistic_explosion.old] & at @s
#
# @within	realistic_explosion:generated_summons/on_item
#

execute if data storage realistic_explosion:main {id:"minecraft:waxed_exposed_copper_golem_statue"} run summon falling_block ~ ~ ~ {Tags:["realistic_explosion.new"],DropItem:0b,BlockState:{Name:"minecraft:waxed_exposed_copper_golem_statue"}}
execute if data storage realistic_explosion:main {id:"minecraft:waxed_weathered_cut_copper_stairs"} run summon falling_block ~ ~ ~ {Tags:["realistic_explosion.new"],DropItem:0b,BlockState:{Name:"minecraft:waxed_weathered_cut_copper_stairs"}}


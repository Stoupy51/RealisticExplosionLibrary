
#> realistic_explosion:v1.2.0/load/confirm_load
#
# @within	realistic_explosion:v1.2.0/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded Realistic Explosion v1.2.0]","color":"green"}
scoreboard players set #realistic_explosion.loaded load.status 1
function realistic_explosion:v1.2.0/load/set_items_storage


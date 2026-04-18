
#> realistic_explosion:v1.2.1/load/confirm_load
#
# @within	realistic_explosion:v1.2.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded RealisticExplosion v1.2.1]","color":"green"}
scoreboard players set #realistic_explosion.loaded load.status 1
function realistic_explosion:v1.2.1/load/set_items_storage


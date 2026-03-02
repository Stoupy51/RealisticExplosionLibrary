
#> realistic_explosion:v1.2.0/load/resolve
#
# @within	#realistic_explosion:resolve
#

# If correct version, load the datapack
execute if score #realistic_explosion.major load.status matches 1 if score #realistic_explosion.minor load.status matches 2 if score #realistic_explosion.patch load.status matches 0 run function realistic_explosion:v1.2.0/load/main


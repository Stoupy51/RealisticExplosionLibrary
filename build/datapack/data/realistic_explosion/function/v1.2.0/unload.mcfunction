
#> realistic_explosion:v1.2.0/unload
#
# @within	#realistic_explosion:unload
#

# Kill entities with custom tags
execute as @e[tag=realistic_explosion.new] at @s run function realistic_explosion:v1.2.0/unload/safe_kill

# Remove scoreboard objectives
scoreboard objectives remove load.status
scoreboard objectives remove realistic_explosion.data

# Clear storages
data remove storage realistic_explosion:main Motion
data remove storage realistic_explosion:main Rotation
data remove storage realistic_explosion:main id


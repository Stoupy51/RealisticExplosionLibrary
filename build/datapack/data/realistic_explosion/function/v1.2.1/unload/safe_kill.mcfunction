
#> realistic_explosion:v1.2.1/unload/safe_kill
#
# @executed	as @e[tag=realistic_explosion.new] & at @s
#
# @within	realistic_explosion:v1.2.1/unload [ as @e[tag=realistic_explosion.new] & at @s ]
#

# This function is used to safely kill entities by teleporting them to the void before killing them to prevent item drops
tp @s ~ -10000 ~
kill @s


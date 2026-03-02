
#> realistic_explosion:v1.2.0/load/enumerate
#
# @within	#realistic_explosion:enumerate
#

# If current major is too low, set it to the current major
execute unless score #realistic_explosion.major load.status matches 1.. run scoreboard players set #realistic_explosion.major load.status 1

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #realistic_explosion.major load.status matches 1 unless score #realistic_explosion.minor load.status matches 2.. run scoreboard players set #realistic_explosion.minor load.status 2

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #realistic_explosion.major load.status matches 1 if score #realistic_explosion.minor load.status matches 2 unless score #realistic_explosion.patch load.status matches 0.. run scoreboard players set #realistic_explosion.patch load.status 0


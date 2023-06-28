
#> realistic_explosion:falling_block/get_motion_from_rotation
#
# @within			realistic_explosion:falling_block/main
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


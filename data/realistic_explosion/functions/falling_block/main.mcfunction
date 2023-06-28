
#> realistic_explosion:falling_block/main
#
# @within			realistic_explosion:generated_summons/all
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
execute positioned 0 0 0 summon marker run function realistic_explosion:falling_block/get_motion_from_rotation

# Apply the motion to the entity
execute store result entity @s Motion[0] double 0.03 run data get storage realistic_explosion:main Motion[0]
execute store result entity @s Motion[1] double 0.03 run data get storage realistic_explosion:main Motion[1]
execute store result entity @s Motion[2] double 0.03 run data get storage realistic_explosion:main Motion[2]

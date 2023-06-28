
#> realistic_explosion:explosion/main
#
# @within			realistic_explosion:explode
# @executed			as the temporary marker & at the explosion origin
#
# @description		Execute the function that will handle the explosion
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

# Add the tag to the marker
tag @s add realistic_explosion.origin

# Add a tag to all current items to prevent them from being selected by the function
tag @e[type=item] add realistic_explosion.old

# Destroy the nearest 27 blocks without dropping anything
fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air replace #realistic_explosion:explodable_blocks

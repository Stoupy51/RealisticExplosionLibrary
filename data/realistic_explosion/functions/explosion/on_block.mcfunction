
#> realistic_explosion:explosion/on_block
#
# @within			realistic_explosion:explosion/main
# @executed			as the temporary marker & at a position of a block to destroy
#
# @input score		#power_state realistic_explosion:data : the power state of the explosion (0, 1, 2 or 3)
#
# @description		Destroys the block if it can be destroyed by the explosion
#

# Depending on the power of the explosion, execute the correct setblock command
execute if score #power_state realistic_explosion.data matches 0 if block ~ ~ ~ #realistic_explosion:no_blast_resistance run setblock ~ ~ ~ air destroy
execute if score #power_state realistic_explosion.data matches 1 if block ~ ~ ~ #realistic_explosion:equal_and_below_1200 run setblock ~ ~ ~ air destroy
execute if score #power_state realistic_explosion.data matches 2 if block ~ ~ ~ #realistic_explosion:equal_and_below_3600000 run setblock ~ ~ ~ air destroy
execute if score #power_state realistic_explosion.data matches 3 if block ~ ~ ~ #realistic_explosion:all run setblock ~ ~ ~ air destroy


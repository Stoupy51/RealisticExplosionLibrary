
#> realistic_explosion:explode
#
# @within			Nothing, this function is manually called by the Library's User
# @executed			as unknown entity & at the explosion origin
#
# @input score		#explosion_power realistic_explosion.data : the power of the explosion
# @input score		#falling_fire realistic_explosion.data : indicates if the explosion should spawn falling block "fire" (default: 0)
#
# @description		Summons a temporary marker and execute the function that will handle the explosion
#
# @warning			This file is auto-generated by the generator script, do not edit it manually!
#

# Create the scoreboard objective if it doesn't exist
scoreboard objectives add realistic_explosion.data dummy

# Execute the function as the temporary marker
execute summon marker run function realistic_explosion:explosion/main

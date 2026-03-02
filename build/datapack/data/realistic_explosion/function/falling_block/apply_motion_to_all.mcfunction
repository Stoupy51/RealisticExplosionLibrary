
#> realistic_explosion:falling_block/apply_motion_to_all
#
# @within	realistic_explosion:generated_summons/on_item 2t [ scheduled ]
#
# @description		Apply the explosion motion to all falling blocks
# 
# @warning			This file is auto-generated, do not edit it manually!
#

# Execute the function as all falling blocks to apply the explosion motion
execute as @e[type=falling_block,tag=realistic_explosion.new] at @s run function realistic_explosion:falling_block/main


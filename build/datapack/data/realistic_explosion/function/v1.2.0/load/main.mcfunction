
#> realistic_explosion:v1.2.0/load/main
#
# @within	realistic_explosion:v1.2.0/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #realistic_explosion.loaded load.status matches 1 run function realistic_explosion:v1.2.0/load/secondary



## Python function that aims to generate .mcfunction files that will handle which falling block will be summoned
## Items and Blocks are retrieved manually from: https://github.com/PixiGeko/Minecraft-generated-data/blob/master/1.20/releases/1.20.1/custom-generated/registries/item.txt

# Imports
import os

# Stop if the execution is not in the same folder as the script
if os.getcwd() != os.path.dirname(os.path.realpath(__file__)):
	print("Please execute this script in the same folder as the script")
	exit()

# Constants
GENERATED_SUMMONS_FOLDER = "generated_summons"


# Return a list of items that are also blocks
def getListFromItemsAndBlock() -> list:
	
	# Open the file "item.txt" and "block.txt" and read the content
	with open("item.txt", "r") as file:
		items = file.read().splitlines()
	with open("block.txt", "r") as file:
		blocks = file.read().splitlines()
	
	# For each item, add it to the final list if it's in the block list
	final_list = []
	for item in items:
		if item in blocks:
			final_list.append(item)
	
	# Return the final list
	return final_list


# Generate the .mcfunction files that will handle which falling block will be summoned
def generateSummonsFiles() -> None:
	
	# Get the list of items that are also blocks
	items = getListFromItemsAndBlock()
	
	# Create the folder if it doesn't exist
	if not os.path.exists(GENERATED_SUMMONS_FOLDER):
		os.makedirs(GENERATED_SUMMONS_FOLDER)

	# Delete the content of the folder (ending with .mcfunction)
	for file in os.listdir(GENERATED_SUMMONS_FOLDER):
		if file.endswith(".mcfunction"):
			os.remove(file)

	# For each item, create a file in the "generated_summons" folder
	for item in items:
		
		# Count the number of letters in the item name
		item_name_length = len(item)

		# Open the file where the command will be written
		with open(f"{GENERATED_SUMMONS_FOLDER}/{item_name_length}.mcfunction", "a") as file:
			
			# Write the command in the file
			file.write(f"execute if data storage realistic_explosion:main {{id:\"{item}\"}} run summon falling_block ~ ~ ~ {{DropItem:0b,BlockState:{{Name:\"{item}\"}}}}\n")
	
	# Print a message to the user
	print("Done")


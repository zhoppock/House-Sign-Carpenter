"""
HouseSign.py - This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
    # Charge for this sign.
    # Number of characters.
    # Color of characters.
    # Type of wood.

# Write assignment and if statements here as appropriate.
charge = 0.00
minimumCharge = 35.00
addedChars = 4.00
numChars = int(input("How many characters? "))
oak = 20.00
pine = 0.00
woodType = input("What kind of wood? ")
blackWhite = 0.00
gold = 15.00
color = input("What color font? ")

if numChars > 0:
    charCharge = (numChars - 5) * addedChars
if (woodType == "oak") and (color == "gold"):
    charge = minimumCharge + charCharge + oak + gold
elif (woodType == "oak") and (color == "blackWhite"):
    charge = minimumCharge + charCharge + oak + blackWhite
elif (woodType == "pine") and (color == "gold"):
    charge = minimumCharge + charCharge + pine + gold
elif (woodType == "pine") and (color == "blackWhite"):
    charge = minimumCharge + charCharge + pine + blackWhite
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))

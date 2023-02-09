# Import a few useful containers from the typing module
from typing import Dict, Union
# Import the class and method needed to create the computer
from computer import *
# Import the class and methods nedded in oo_resale_shop.py
from oo_resale_shop import *
# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

def main():

    # First, let's make a computer
    computer1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    # Creates a dictionary using the information on the computer
    computer1_dict = computer1.create_comp_dict()

    # Making a second computer 
    computer2 = Computer("Lenovo",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "Ryzen 5000 Series", 2013, 100)

    # Creates a dictionary using the information on the computer
    computer2_dict = computer2.create_comp_dict()

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    ComputerCo = ResaleShop()
    computer_id_1 = ComputerCo.buy(computer1_dict)
    print("Buying", computer1.description)
    print("Adding to inventory...")
    print("Done.\n")
    
    # Creates a dictionary using the information on the computer
    computer_id_2 = ComputerCo.buy(computer2_dict)
    print("Buying", computer2.description)
    print("Adding to inventory...")
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ComputerCo.print_inventory()
    print("Done.\n")
    
    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id_1, ", updating OS to", new_OS)
    print("Updating inventory...")
    ComputerCo.refurbish(1, new_OS)
    print("Done.\n")

    # Updating the price
    new_price = 2000
    print("Updating Price of Item ID:", computer_id_1, "to", new_price )
    ComputerCo.update_price(computer_id_1, new_price)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ComputerCo.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id_1)
    ComputerCo.sell(1)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ComputerCo.print_inventory()
    print("Done.\n")

    

# Calls the main() function when this file is run
if __name__ == "__main__": main()

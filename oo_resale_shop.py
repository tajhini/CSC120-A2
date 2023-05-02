"""
   Filename: oo_resale_shop.py
Description: Object oriented program for a resale shop
     Author: Tajhini Brown
       Date: Feb 8 2022
       
"""


"""
Creates a class that has methods to carry out the sale and resale of computer objects 
"""
class ResaleShop:
    
    def __init__(self) -> None:
        """
        Creates an inventory of computers
        """
        self.computer_inventory = [] #inventory of computers

        
    def buy(self, computer_dict: dict) -> int:
        """
        Takes in a dictionary containing all the information about a computer,
        adds it to the computer_inventory, returns the assigned item_id

        :param computer_dict: (dict) computer object dictionary
        :return : (int) the assigned item_id
  
        """
        self.computer_inventory.append(computer_dict)
        item_id = self.computer_inventory.index(computer_dict)
        return item_id
        
    
    def print_inventory(self) -> None:
        """
        prints all the items in the inventory (if it isn't empty), prints error otherwise

        :param : None
        :return : None
        """
        # If the inventory is not empty
        if self.computer_inventory:
        # For each item
            for item in self.computer_inventory:
                # Print its details
                print(f'Item ID: {self.computer_inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")
       
    
    def refurbish(self, item_ID: int, new_os: str) -> None:
        """
        Takes in an item_ID and a new operating system, updates the operating system of the
        computer if it is the computer_inventory, prints error message otherwise

        :param item_ID: (int) The item id of the computer object
        :param new_os: (str) The new operating system of the computer object
        :return : None
        """

        if self.computer_inventory[item_ID] in self.computer_inventory:
                computer = self.computer_inventory[item_ID] # locate the computer
                if int(computer["year_made"]) < 2000:
                    computer["price"] = 0 # too old to sell, donation only
                elif int(computer["year_made"]) < 2012:
                    computer["price"] = 250 # heavily-discounted price on machines 10+ years old
                elif int(computer["year_made"]) < 2018:
                    computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    computer["price"] = 1000 # recent stuff

                if new_os is not None:
                    computer["operating_system"] = new_os # update details after installing new OS
        else:
                print("Item", item_ID, "not found. Please select another item to refurbish.")
    
    
    def update_price(self, item_ID: int, new_price: int) -> None:
        """
        Takes in an item_ID and a new price, updates the price of the associated
        computer if it is the computer_inventory, prints error message otherwise

        :param item_ID: (int) The item id of the computer object
        :param new_price: (int) The new price of the computer object
        :return : None
        """
        if self.computer_inventory[item_ID] in self.computer_inventory:
            self.computer_inventory[item_ID]["price"] = new_price #assigns the new price as the new value for price
        else:
            print("Item", item_ID, "not found. Cannot update price.")

    
    def sell(self, item_ID: int) -> None:
        """
        Takes in an item_ID, removes the associated computer if it is the inventory, 
        prints error message otherwise

        :param item_ID: (int) The item id of the computer object
        :return : None
        """
        if self.computer_inventory[item_ID] in self.computer_inventory:
            del self.computer_inventory[item_ID]
            print("Item", item_ID, "sold!")
        else: 
            print("Item", item_ID, "not found. Please select another item to sell.")
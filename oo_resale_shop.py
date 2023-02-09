# Increment each time a new computer is added. 
item_id = 0

# Creates a class that acts as an inventory for the computer objects.
class ResaleShop:

    def __init__(self) -> None:
        self.computer_inventory = {} #inventory of computers

    """
        Takes in a Dict containing all the information about a computer,
        adds it to the computer_inventory, returns the assigned item_id
    """
    def buy(self, computer_dict: dict) -> int:
        global item_id
        item_id += 1 # increment itemID
        self.computer_inventory[item_id] = computer_dict
        return item_id
        
    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self) -> None:
        # If the inventory is not empty
        if self.computer_inventory:
        # For each item
            for item_ID in self.computer_inventory:
                # Print its details
                print(f'Item ID: {item_ID} : {self.computer_inventory[item_ID]}')
        else:
            print("No inventory to display.")
       
    """
    Takes in an item_ID and a new operating system, updates the operating system of the
    computer if it is the computer_inventory, prints error message otherwise
    """
    def refurbish(self, item_ID: int, new_os: str) -> None:

        if item_ID in self.computer_inventory:
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
    
    """
    Takes in an item_ID and a new price, updates the price of the associated
    computer if it is the computer_inventory, prints error message otherwise
    """
    def update_price(self, item_ID: int, new_price: int) -> None:
        if item_ID in self.computer_inventory:
            self.computer_inventory[item_ID]["price"] = new_price #assigns the new price as the new value for price
        else:
            print("Item", item_ID, "not found. Cannot update price.")

    """
    Takes in an item_ID, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_ID: int) -> None:
        if item_ID in self.computer_inventory:
            del self.computer_inventory[item_ID]
            print("Item", item_ID, "sold!")
        else: 
            print("Item", item_ID, "not found. Please select another item to sell.")
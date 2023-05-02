
"""
    Creates a base class for the computer objects
"""
class Computer:
    #declaration of the data types
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.processor_type = processor_type 
        self.description = description
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    
    def create_comp_dict(self) -> dict:
        """
        Takes in specifications about a computer and returns a dictionary with 
        the key describring the type of specification the value is.

        :return : (dict) a dictionary containing the specifications of the computer
  
        """
        return {'description': self.description,
            'processor_type': self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price
    }

   
    



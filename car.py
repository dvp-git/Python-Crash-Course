## Contains the class Car

class Car():
    """Making of the car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

        
    def get_descriptive_name(self):
        """Print a descriptive name of the car"""
        print("Presenting : " + str(self.year) + " , "  + self.model +  self.make)
        
    def read_odometer(self):
        """Get the odometer reading"""
        print("This car has " + str(self.odometer_reading)  + " miles on it")
        
    def update_odometer(self,miles):
        """Update the odometer reading on the car"""
        self.odometer_reading = miles

    def increment_odometer(self,miles):
        """Add the miles to the odometer of the car"""
        self.odometer_reading  += miles



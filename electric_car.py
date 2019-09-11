## Making an ElectricCar Class :



from car import Car

class ElectricCar(Car):
    """Describe the features of an electric Car"""
    def __init__(self , make, model, year):
        super().__init__(make ,model ,year)
        self.battery = Battery()

##Making a class Battery
class Battery():
    """the battery size and the range depending on the size"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_battery_info(self):
        print("This battery has " + str(self.battery_size) + " -kWH")

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size >= 85:
            range = 280
        print("The car can go " + str(range) + " on a full charge")

## Exercise 9.9 Battery Upgrade

## Making a class called Car

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


## Making an ElectricCar Class :

class ElectricCar(Car):
    """Describe the features of an electric Car"""
    def __init__(self , make, model, year):
        super().__init__(make ,model ,year)
        self.battery = Battery()


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
        

## Starting the code

my_electric_car = ElectricCar('metallic','Gen4',2019)

##Getting the default set parameters of the car
my_electric_car.get_descriptive_name()
my_electric_car.read_odometer()

##Updating the car Odometer miles
my_electric_car.update_odometer(30)
my_electric_car.read_odometer()

##Incrementing the miles on the car
my_electric_car.increment_odometer(50)
my_electric_car.read_odometer()

### Getting the battery info
my_electric_car.battery.get_battery_info()

##Get range of car
my_electric_car.battery.get_range()

###Upgrading the battery
my_electric_car.battery.upgrade_battery()

### Getting the battery info after battery upgrade
my_electric_car.battery.get_battery_info()

##Get range of car after battery upgrade
my_electric_car.battery.get_range()

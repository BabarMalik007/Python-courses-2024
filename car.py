class Car():
    def __init__(self,make,model,year="2024"):
        self.make  = make
        self.model = model
        self.year  = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
       return f"{self.year} {self.make} {self.model}".title()

    def set_odometer(self, new_reading):
        if new_reading < self.odometer_reading:
            print("Cheater insaan ban jaa.")
        else:
            self.odometer_reading = new_reading

    def get_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def fill_gas_tank(self):
        print("Ok car tank has being filled with gasoline")

class Battery():
    def __init__(self,make ,price,watts,plates, size):
        self.make = make
        self.price = price
        self.watts = watts
        self.plates = plates
        self.size = size
    def desc_battery(self):
        print(f"{self.make} {self.price} {self.watts} {self.plates} {self.size}")

class ElectricCar(Car):
    def __init__(self,make, model , year):
        super().__init__(make, model , year)
        self.battery = Battery("Exide", 50000,2000,27,70)
   
    def fill_gas_tank(self):
        print("There is no gas tank needed in thr Electric Car")
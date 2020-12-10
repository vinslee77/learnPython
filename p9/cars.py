class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_info(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def updata_odometer(self, miles):
        if miles < self.odometer_reading:
            print("You cannot roll back the odometer!")
        else:
            self.odometer_reading = miles

    def increase_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_info())
# my_new_car.odometer_reading = 18
my_new_car.updata_odometer(18)
my_new_car.read_odometer()

my_new_car.increase_odometer(17)
my_new_car.read_odometer()

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
     
     # Child class
     
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_electric = ElectricCar("Tesla","Model S","85kwh")
print(my_electric.full_name())
print(my_electric.battery_size)
print(my_electric.brand)
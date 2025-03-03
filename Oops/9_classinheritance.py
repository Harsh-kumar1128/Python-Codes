class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Desel"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric fuel"

my_tesla = ElectricCar("Tata","Ëlectric Car","90kwh")

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
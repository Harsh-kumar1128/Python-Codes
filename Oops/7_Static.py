class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand
    
    @staticmethod                 #decorators
    def general_descrtion():
        return "Car are means of transport"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tata","Ëlectric Car","90kwh")
print(my_tesla.general_descrtion())

print(Car.general_descrtion())

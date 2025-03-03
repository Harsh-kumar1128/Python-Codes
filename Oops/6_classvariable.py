class Car:
    totalcar = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.totalcar += 1
        
    def get_brand(self):
        return self.__brand
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Desel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Petrol or Desel"
    

my_tesla = ElectricCar("Tata","Ëlectric Car","90kwh")    # iske andar bhi  Car class ka objkect hai
Car("Abc","Zkcxkj")

print(my_tesla.totalcar)
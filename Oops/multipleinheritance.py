class Car:       #class
   def __init__(self,brand,model):      #constructor
      self.brand = brand
      self.model = model

class Battery:
   def battery_info(self):
      return "This is battery"
   
class Emgine:
   def engine_info(self):
      return "This is Emgine"
   
class ElectricCarTwo(Car,Battery,Emgine):
   pass

my_tesla = ElectricCarTwo('Tesla','Model S')
print(my_tesla.battery_info())
print(my_tesla.engine_info())

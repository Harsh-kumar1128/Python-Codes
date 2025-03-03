class Car:       #class
   def __init__(self,brand,model):      #constructor
      self.brand = brand
      self.model = model

my_car = Car("Tesla","Model S")        #object created
print(my_car.brand)
print(my_car.model)
      
my_new_car = Car("Tata","Safari")
print(my_new_car.model)
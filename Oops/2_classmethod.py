class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):         #Method
        return f"{self.brand} {self.model}"

my_tesla = Car("Tesla","Model S")
print(my_tesla.full_name())
print(my_tesla.brand)
    
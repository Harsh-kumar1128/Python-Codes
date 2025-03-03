class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    def get_brand(self):
        return self.__brand
    
    @staticmethod                 #decorators
    def general_descrtion():
        return "Car are means of transport"
    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"    #formating string
    @property
    def model(self):
        return self.__model
    

car = Car('Tata','Nano')
print(car.full_name())
#ar.model = 'Safari'
print(car.model)

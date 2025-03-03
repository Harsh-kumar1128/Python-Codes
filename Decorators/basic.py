def basic(func):
    def wrapper(*args,**kwargs):
        print("Decorators is calling")
        return func(*args,**kwargs)
        
    return wrapper

@basic
def Hello(a,b):
    print('Hello Decorators')
    return a+b

print(Hello(5,6))
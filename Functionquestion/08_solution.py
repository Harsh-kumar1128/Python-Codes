def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_kwargs(name='harsh',power='laser')
print_kwargs(name='Python')

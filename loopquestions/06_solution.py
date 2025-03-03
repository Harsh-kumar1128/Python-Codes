number = int(input('Enter the number for factorial : '))
fact = 1
while number > 0:
    fact = fact * number
    number -= 1
    print('Factorial',fact)
     
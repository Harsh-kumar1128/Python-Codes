input_str = input('Enter name that you want to check for charcter is repeat : ')

for char in input_str :
    print(char)
    if input_str.count(char) == 1:
        print('char is ', char)
        break
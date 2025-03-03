year = int(input('Enter year that you want to check for leap year or not '))

if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
    print(year,'Is a leap year')
else :
    print('Year is not leap year')
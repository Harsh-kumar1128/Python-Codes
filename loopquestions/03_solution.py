number = int(input('Enter number for table :'))

for i in range(1,11):
    if i == 5 :
        continue
    print(number,'x',i,'=',number*i)
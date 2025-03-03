age = int(input("Enter you age: "))
day = input("Enter Day :").upper()
Price = 12 if age >= 18 else 8


if day == 'WEDNESDAY':
 Price -= 2
 print("Wedneaday Ticket Price is ",Price)
else :
 print("Your price for Ticket is $" , Price)

 


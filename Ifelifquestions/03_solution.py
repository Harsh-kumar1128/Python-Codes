score = int(input("Enter your score number : "))

if score >=101 :
    print("Please verify your score")
    exit()

if score >=90 :
    Grade = 'A'

elif score >=80:
    Grade = 'B'
elif score >=70:
    Grade = 'C'
elif score >=60:
    Grade = 'D'
else : 
    Grade = 'F'
print("Your Grade is :",Grade)
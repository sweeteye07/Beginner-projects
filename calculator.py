print("--------------CALCULATOR------------------")

number1 = float(input("Enter any number : "))
number2 = float(input("Enter any number : "))

print("Enter 1 for adition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for Division")

choice = int(input("Enter number between 1 to 4 : "))

if choice == 1 :
    print("The sum of given two number is ",number1+number2)
elif choice == 2 :
    print("The Subtraction of given two number is ", number1-number2)
elif choice == 3 :
    print("The Multiplication of given two number is", number1*number2 )
elif choice == 4 :
    print("The Division of given two number is",number1/number2 )
else :
    print("INVALID REQUEST")


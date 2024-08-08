
print("Welcome to The Number guessing game !")


import math
import random
A = 1
B = 100
X = random.randint(A,B)
print("You have only ",round(math.log(B - A + 1 ,2)),"Chances to guess the number ! \n")

count = 0
while count < math.log(B - A + 1 , 2):
    count += 1
    guess = int(input("Guess the number :>"))
    if X == guess :
        print("Congratulations you guessed the number in ", count , " tries ")
        break
    elif X > guess :
        print("You guessed too small ! , try for a bigger number ;) ")
    elif X < guess :
        print("You guessed too high ! , try for a smaller number :/")

if count >= math.log(B - A + 1 , 2):
    print(f"The number is {X}")
    print("\n Better luck next time ! ")
import random 
def gameWIN(bot,user):
    if bot == user :
        return None
    elif bot == 'S':                    # S = Stone
        if user == 'P':                 # P = Paper
            return True
        elif user == 'SC':              #SC = scissors
            return False
    elif bot == 'P':
        if user == 'S':
            return False
        elif user =='SC':
            return True 
    elif bot == 'SC':
        if user =='S':
            return True
        elif user == 'P':
            return False


print("Bot Turn : Stone(S) Paper(P) Scissor(SC) ?")

list_1=["S","P","SC"]
bot = random.shuffle(list_1)
bot=list_1[0]

user = input("Your turn : Stone(S) Paper(P) Scissor(SC) ? \n")
a = gameWIN(bot,user)

print(f"Bot chose {bot}")
print(f"You chose {user}")

if a == None:
    print("The game is a tie !")
elif a :
    print("You win !")
else :
    print("You Lose dumbass !")

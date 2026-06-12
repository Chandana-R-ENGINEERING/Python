# Mini Project Guess Number

import random

Target=random.randint(1,100)

while True:
    userchoice=input("Guess the Target or Quit: ")
    if(userchoice=="Quit"):
        break
    userchoice = int(userchoice)
    if(userchoice == Target):
        print("Success: Correct Guess!!")
        break
    
    elif (userchoice < Target):
        print("Your number was too small. Take  a Bigger Guess......")
    else:
        print("Your number was too big. Take  a Smaller Guess........")



print("-----------------GAME OVER--------------------")
    
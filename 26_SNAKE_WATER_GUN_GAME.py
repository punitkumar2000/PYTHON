#SNAKE WATER GUN

import random

lst = ['s', 'w', 'g']

Chance = 10
No_of_Chance = 0
Computer_Point = 0
Human_Point = 0

print(" \t \t \t \t Snake,Water,Gun Game")
print("s for Snake:\nw for Water:\ng for Gun:\n")

# making the game in while
while No_of_Chance < Chance:
    Input = input('Snake,Water,Gun:')
    Random = random.choice(lst)

    if Input == Random:
        print("Tie Both 0 Point to Each \n ")

    # if user enter s
    elif Input == "s" and Random == "g":
        Computer_Point = Computer_Point + 1
        print(f"Your Guess {Input} and Computer Guess is {Random} \n")
        print("Computer Wins 1 Point \n")
        print(f"Computer_Point is {Computer_Point} and Your Point is {Human_Point} \n ")

    elif Input == "s" and Random == "w":
        Human_Point = Human_Point + 1
        print(f"Your Guess {Input} and Computer Guess is {Random} \n")
        print("Human Wins 1 Point \n")
        print(f"Computer_Point is {Computer_Point} and Your Point is {Human_Point} \n")

    # if user enter w
    elif Input == "w" and Random == "s":
        Computer_Point = Computer_Point + 1
        print(f"Your Guess {Input} and Computer Guess is {Random} \n")
        print("Computer Wins 1 Point \n")
        print(f"Computer_Point is {Computer_Point} and Your Point is {Human_Point} \n ")

    elif Input == "w" and Random == "g":
        Human_Point = Human_Point + 1
        print(f"Your Guess {Input} and Computer Guess is {Random} \n")
        print("Human Wins 1 Point \n")
        print(f"Computer_Point is {Computer_Point} and Your Point is {Human_Point} \n")

    # if user enter g

    elif Input == "g" and Random == "s":
        Human_Point = Human_Point + 1
        print(f"Your Guess {Input} and Computer Guess is {Random} \n")
        print("Human Wins 1 Point \n")
        print(f"Computer_Point is {Computer_Point} and Your Point is {Human_Point} \n")


    elif Input == "g" and Random == "w":
        Computer_Point = Computer_Point + 1
        print(f"Your Guess {Input} and Computer Guess is {Random} \n")
        print("Computer Wins 1 Point \n")
        print(f"Computer_Point is {Computer_Point} and Your Point is {Human_Point} \n ")

    else:
        print("You Have Entered Wrong Input\n")

    No_of_Chance = No_of_Chance + 1
    print(f"{Chance - No_of_Chance} is Left Out of {Chance} \n")

print("Game Over")

if Computer_Point == Human_Point:
    print("Tie")

elif Computer_Point > Human_Point:
    print("Computer Wins and You Loose")

else:
    print("You Win and Computer Loose")

print(f"Your Point is: {Human_Point} and Computer Point: is {Computer_Point}")





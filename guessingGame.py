import random

number = random.randint(1,9)
guess = input("Please enter your guess")

chances = 5

while chances < 5 and > 1 :
    if guess == number:
        print("CONGRATULATIONS YOU WON !!!")
    else:
        print("You were close. " + "Guess a number higher than" + number - 3)
break

while chances < 1:
    print("You Lose, " + "The number is " + number)
break

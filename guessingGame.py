import random

number = random.randint(1,9)
guess = input("Please enter your guess")

chances = 5

while chances < 5 and > 1:
    if guess == number:
        print("CONGRATULATIONS YOU WON !!!")
    else:
        print("You Lose  The number is " + number)
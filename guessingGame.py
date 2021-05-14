import random

number = random.randint(1,9)

chances = 5

print(number)

while (chances > 0) :

    guess = int(input("Please enter your guess"))

    if guess == number:
        print(guess)
        print("CONGRATULATIONS YOU WON !!!")
        break
    else:
        print("You lose. " + "Try again")
    chances = chances - 1

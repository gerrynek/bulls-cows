import time

from unique_number import uniqueFourDigitNumber

#Welcome message
print(
"""Welcome to Bulls&Cows!\n
I've generated 4 digit number with unique digits for your entertainment
Let's play Bulls and Cows game.
""")
input("\nPress Enter when you are ready\n")

#Initialize variables
start = time.time()
number = uniqueFourDigitNumber()
print(number)
bulls = 0
cows = 0
no_of_guesses = 0

#Translates
guess_tr = "guess"
cows_tr = "cow"
bulls_tr = "bull"

#The game
while True:
    guess = input("\nPlease enter a 4 digit number: ")
    no_of_guesses += 1
    if no_of_guesses>1:
        guess_tr = "guesses"
    if len(guess) == 4:
        if guess == number:
            end = time.time()
            print(f"""Correct, you've guessed the right number in
    {no_of_guesses} {guess_tr}! It took you {round(end - start, 2)} seconds.""")
            break

        for digit in guess:
            if digit in number:
                cows += 1

        for digit in guess:
            if guess.find(digit) == number.find(digit):
                bulls += 1
                cows -= 1

        if cows > 1 or cows == 0:
            cows_tr = "cows"

        if bulls > 1 or bulls == 0:
            bulls_tr = "bulls"

        print(cows_tr, ":", cows, ",", bulls_tr, ":", bulls)
        cows = 0
        bulls = 0
    else:
        print("Enter 4 digit number!")
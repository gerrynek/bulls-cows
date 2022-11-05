from logic import uniqueFourDigitNumber

print(
    """Welcome to Bulls&Cows!\n
I've generated 4 digit number for your entertainment
Let's play Bulls and Cows game.""")

input("\nPress enter when you are ready\n")

number = uniqueFourDigitNumber()
print(number)
bulls = 0
cows = 0
no_of_guesses = 0
guess_tr = "guess"

while True:
    guess = input("Please enter a 4 digit number: ")
    no_of_guesses += 1

    if no_of_guesses>1:
        guess_tr = "guesses"

    if guess == number:
        print(f"Correct, you've guessed the right number in {no_of_guesses} {guess_tr}!")
        break
    for digit in guess:
        if digit in number:
            cows += 1

    for digit in guess:
        if guess.find(digit) == number.find(digit):
            bulls +=1

    print("cows: ", cows, ", bulls: ", bulls)
    cows = 0
    bulls = 0
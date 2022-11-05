import random

def uniqueFourDigitNumber():
    number = ""
    digit = ""
    extra_guess = 0

    while len(number)<4:
        digit = str(random.randint(0, 9))
        if digit not in number:
            number += digit
        if number[0] == "0":
            number = ""
    return number

print(uniqueFourDigitNumber())
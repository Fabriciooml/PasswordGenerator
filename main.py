from string import ascii_letters
from random import randint, choice, shuffle

def RandomLetter():
    lower_upper_alphabet = ascii_letters
    random_letter = choice(lower_upper_alphabet)
    return random_letter

def RandomNumber():
    random_number = randint(0, 9)
    return random_number

def GeneratePassword(howLong):
    password = []
    finalPassword = []
    numberOfLetters = randint(1,howLong)
    numberOfNumbers = howLong - numberOfLetters
    for i in range(numberOfLetters):
        password.append(RandomLetter())
    for j in range(numberOfNumbers):
        password.append(str(RandomNumber()))

    shuffle(password)
    finalPassword = "".join(password)
    return finalPassword

def UserInteract():
    wantPassword = input("Want a password? (y/n)\n")
    while(wantPassword == "y"):
        howLong = int(input("How long it will be? (min 6)\n"))
        if(howLong >= 6):
            print("Generating...")
            password = GeneratePassword(howLong)
            print("Your Password is: {}".format(password))
            break
        else:
            print("Minimum 6, please")

UserInteract()

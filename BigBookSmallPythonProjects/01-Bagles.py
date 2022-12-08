from random import *

randomNumber = randint(100, 999)

guessesLeft = 10
for i in range(guessesLeft):
    remainingGuess = guessesLeft - i
    print("Guess the 3 digit number. You have {} tries.".format(remainingGuess))
    userGuess = input("Enter your guess: ")

    if userGuess == randomNumber:
        print("Correct!")
        break
    #elif Fermi:     # one number is correct and in the right position 
        print("Fermi")
    #elif Pico:      # one number is correct but in the wrong position
        print("Pico")
    #elif Bagles:    # no correct number 
        print("Bagles")


def seeDigit(digit):
    hundreds = digit//100                   # Gets the hundreds digit

    tens = (digit-(hundreds*100))//10       # Gets the tens digit       

    ones = digit-(hundreds*100)-(tens*10)   # Gets the ones digit

    return [hundreds, tens, ones]

print(seeDigit(123))
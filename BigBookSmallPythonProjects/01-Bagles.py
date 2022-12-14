from random import *

def main():
    randomNumber = randint(100, 999)
    guessesLeft = 10

    print(randomNumber)
    for i in range(guessesLeft):        
        remainingGuess = guessesLeft - i
        print("\nGuess the 3 digit number. You have {} tries.".format(remainingGuess))
        
        userGuess = int(input("Enter your guess: "))
        while (userGuess>999 or userGuess<100):     # checks if the input is only 3 digit number
            print("Value too large or small.\n")
            userGuess = int(input("Enter your guess: ")) 

        if userGuess == randomNumber:
            print("Correct!")
            break
        else:
            if PFB(userGuess, randomNumber):
                multiplier = pico(userGuess,randomNumber)
                print("Pico "*multiplier)
            elif fermi(userGuess):
                multiplier = fermi(userGuess,randomNumber)
                print("Fermi"*multiplier)
            else:
                print("Bagels")

    print("You lose. The answer is {}.".format(randomNumber))

def PFB(userInput, generatedNum):
    list_1 = seeDigit(userInput)            # listed user input
    list_2 = seeDigit(generatedNum)         # listed randomly generated value
    check = any(digit in list_1 for digit in list_2)
    if check == True:                     # confirms if a digit is in list 1 is in list 2
        for digit in list_1:   
            n=0
            # FERMI
            if digit == list_2[n]:  # if a digit in list 1 is same with its corresponding index in list 2, fermi
                return 1
            # PICO
            if digit != list_2[n]:  # if a digit in list 1 is not same with its corresponding index in list 2, fermi
                return 2
            n+=1
    

def seeDigit(digit):
    hundreds = digit//100                   # Gets the hundreds digit
    tens = (digit-(hundreds*100))//10       # Gets the tens digit       
    ones = digit-(hundreds*100)-(tens*10)   # Gets the ones digit
    return [hundreds, tens, ones]

def fermi(userInput, generatedNum):
    list_1 = seeDigit(userInput)            # listed user input
    list_2 = seeDigit(generatedNum)         # listed randomly generated value
    check = any(digit in list_1 for digit in list_2)
    similarCounter = 0 
    if check == True:                       # confirms if a digit is in list 1 is in list 2
        for digit in list_1:   
            n=0
            if digit == list_2[n]:  # if a digit in list 1 is same with its corresponding index in list 2, fermi
                similarCounter+=1
            n+=1
    return similarCounter

def pico(userInput, generatedNum):
    list_1 = seeDigit(userInput)            # listed user input
    list_2 = seeDigit(generatedNum)         # listed randomly generated value
    check = any(digit in list_1 for digit in list_2)
    similarCounter = 0 
    if check == True:                       # confirms if a digit is in list 1 is in list 2
        for digit in list_1:
            n=0
            if digit != list_2[n]:  # if a digit in list 1 is not same with its corresponding index in list 2, pico
                similarCounter+=1
            n+=1
    return similarCounter

def bagels(userInput, generatedNum):
    list_1 = seeDigit(userInput)            # listed user input
    list_2 = seeDigit(generatedNum)         # listed randomly generated value
    check = any(digit in list_1 for digit in list_2)
    if check != False:
        return True

if __name__ == '__main__':
    main()
# print(seeDigit(123))
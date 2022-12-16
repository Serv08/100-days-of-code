from random import *

def main():
    randomNumber = randint(100, 999)
    guessesLeft = 10

    print("Guess the number")
    print("Fermi if a digit is right and in correct position\nPico if a digit is right but in wrong position\nBagles if none of the digits are correct")

    # print(randomNumber)
    for i in range(guessesLeft):        
        remainingGuess = guessesLeft - i
        print("\n\nGuess the 3 digit number. You have {} tries.".format(remainingGuess))
        
        userGuess = int(input("Enter your guess: "))
        while (userGuess>999 or userGuess<100):     # checks if the input is only 3 digit number
            print("Value too large or small.\n")
            userGuess = int(input("Enter your guess: ")) 

        if userGuess == randomNumber:
            print("Correct!")
            break
        else:
            list_1 = seeDigit(userGuess)            # listed user input
            list_2 = seeDigit(randomNumber)         # listed randomly generated value
            check = any(digit in list_1 for digit in list_2)
            if check == True:                     # confirms if a digit is in list 1 is in list 2
                for i in range(len(list_1)):
                    if list_1[i] == list_2[i]:
                        print("Fermi", end=" " )
                    else:
                        for j in range(len(list_1)):
                            if list_1[i] == list_2[j]:
                                print("Pico", end=" ")
            else:
                print("Bagels", end="")
    print("The answer is {}.".format(randomNumber))

def seeDigit(digit):
    hundreds = digit//100                   # Gets the hundreds digit
    tens = (digit-(hundreds*100))//10       # Gets the tens digit       
    ones = digit-(hundreds*100)-(tens*10)   # Gets the ones digit
    return [hundreds, tens, ones]

if __name__ == '__main__':
    while True:
        main()
        ans = input("\nDo you want to play again? (yes or no): ")
        if ans == "no":
            print("Thanks for playing!")
            break
## Homework 1 - Python Programming
## Kevin Buckley
## 9/8/14
#
# Guess the Number: Think of random # 1-100, computer guesses until correct

# Boolean flag for looping through game cycle
quitNow = False

while (not quitNow):
    name = input("Hello, what is your name? ")
    print("Hi " + name + " we're going to play a game!")
    print("Think of a random number 1 to 100, and I will guess it.")

    # Set initial guess to 50, lower bound to 1, upper bound to 100
    guess = 50
    lBound = 1
    uBound = 100

    # Set the boolean found flag to false, and the attempt counter at 1 
    found = False
    counter = 1

    # Loop until the number is found
    while (not found):
        correct = input("Is your number " + str(guess) + "? (y/n): ")
        if (correct == "y" or correct == "Y"):
            ## guessed correctly!
            found = True
            print("See? I told you I'd guess it! In only " + str(counter) +
                  " tries!")        
        elif (correct == "n" or correct == "N"):
            ##  process incorrect guess
            counter += 1
            validIn = False
            while(not validIn):
                correct = input("Is your number higher than " + str(guess) +
                                "? (y/n): ")
                if (correct == "y" or correct == "Y"):
                    # process higher number (add 50% (floored) to guess)
                    validIn = True
                    lBound = guess
                    # where guess is not = 99
                    if (guess != 99):
                        guess = (uBound - lBound)//2 + guess
                    else:
                        # boundary condition
                        guess = 100
                elif (correct == "n" or correct == "N"):
                    # process lower number (divide guess in half)
                    validIn = True
                    uBound = guess
                    # where guess is not = 2
                    if (guess != 2):
                        guess -= (uBound - lBound)//2
                    else:
                        # boundary condition
                        guess = 1                            
                else:
                    #process invalid input
                    print("Invalid input, please input 'y' for yes or " +
                          "'n' for no.")
        else:
            ##  process invalid input
            print("Invalid input, please input 'y' for yes or 'n' for no.")

    # After number found, prompt to play again
    validIn = False
    while(not validIn):
        correct = input("Would you like to continue playing? (y/n): ")
        if (correct == "y" or correct == "Y"):
            # choose to continue playing (do nothing)
            validIn = True
        elif (correct == "n" or correct == "N"):
            # choose to quit
            validIn = True
            quitNow = True
        else:
            # handle invalid input
            print("Invalid input, please input 'y' for yes or 'n' for no.")

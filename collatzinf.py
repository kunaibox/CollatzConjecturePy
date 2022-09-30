#Kunaibox
import random
import sys
import time
loop = True #starts a loop
while loop == True: #starts a loop
    print("1. Manual input")
    print("2. Infinite random")
    choice = int(input("Choose: "))
    if choice == 1:
        startnumber = int(input("Any number for collatz conjecture: ")) #input for conjecture
        result = 0
        def collatz(startnumber): #function for conjecture
            while startnumber != 1: #checks if number is one so it ends the formula loop
                if startnumber % 2 == 0: #checks if even
                    result = startnumber
                    startnumber = startnumber/2 #divides by 2 if even
                    print(result,"/ 2 =",startnumber) #prints outcome
                elif startnumber % 2 == 1: #checks if odd
                    result = startnumber
                    startnumber = startnumber*3+1 #multiplies by 3 and adds one
                    print(result,"* 3 + 1 =",startnumber) #prints the outcome
        collatz(startnumber) #calls upon the collatz function

    elif choice == 2:
        print("Are you sure you want to proceed?")
        print("This version creates a random int from 0 to the max number size available by computer")
        print("I dont take any responsability for damage that you might cause")
        print("Would you like to push your computer to the max?")
        print("To stop the program use ctrl+c")
        yesno = input("Y/N")
        if yesno.lower() == "y":
            print("1. Slow mode")
            print("2. Fast mode(unstable)")
            choicee = int(input("Choose: "))
            if choicee == 1:
                result = 0
                on = True
                while on == True:
                    startnumber = random.randint(0,sys.maxsize) #input for conjecture
                    def collatz(startnumber): #function for conjecture
                        while startnumber != 1: #checks if number is one so it ends the formula loop
                            if startnumber % 2 == 0: #checks if even
                                result = startnumber
                                startnumber = startnumber/2 #divides by 2 if even
                                print(result,"/ 2 =",startnumber) #prints outcome
                            elif startnumber % 2 == 1: #checks if odd
                                result = startnumber
                                startnumber = startnumber*3+1 #multiplies by 3 and adds one
                                print(result,"* 3 + 1 =",startnumber) #prints the outcome
                    collatz(startnumber) #calls upon the collatz function
                    time.sleep(1)
            elif choicee == 2:
                    startnumber = random.randint(0,sys.maxsize) #input for conjecture
                    def collatz(startnumber): #function for conjecture
                        while startnumber != 1: #checks if number is one so it ends the formula loop
                            if startnumber % 2 == 0: #checks if even
                                result = startnumber
                                startnumber = startnumber/2 #divides by 2 if even
                                print(result,"/ 2 =",startnumber) #prints outcome
                            elif startnumber % 2 == 1: #checks if odd
                                result = startnumber
                                startnumber = startnumber*3+1 #multiplies by 3 and adds one
                                print(result,"* 3 + 1 =",startnumber) #prints the outcome
                    collatz(startnumber) #calls upon the collatz function
        elif yesno.lower == "n":
            print("Thank you")
    else:
        print("Wrong choice")


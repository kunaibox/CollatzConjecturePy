import random

loop = True
while loop == True:
    startnumber = int(input("Any number for collatz conjecture: "))
    def collatz(startnumber):
        while startnumber != 1:
            if startnumber % 2 == 0:
                startnumber = startnumber/2
                print(startnumber)
            elif startnumber % 2 == 1:
                startnumber = startnumber*3+1
                print(startnumber)
    collatz(startnumber)




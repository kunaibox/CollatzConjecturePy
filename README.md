# Collatz Conjecture
### Unsolved problem in mathematics: Does the Collatz sequence eventually reach 1 for all positive integer initial values? The Collatz conjecture is one of the most famous unsolved problems in mathematics.
![picture](https://d2r55xnwy6nx47.cloudfront.net/uploads/2019/12/CollatzGraph_1300Lede.jpg)
## The rules for the Collatz Conjecture
### If the number is even you divide by two, if its odd you multiply it by 3 and add a one. 
>C(n) = (3n+1)/2^x
## How this program works
### At first it starts an infnite loop
![Loop](https://cdn.discordapp.com/attachments/875826551571222538/1025399573327396925/unknown.png)
### Then we have an int input which allows the user to input any number for the collatz conjecture to apply the formula
![Input](https://cdn.discordapp.com/attachments/875826551571222538/1025399921823723661/unknown.png)
### We create a function that applies the formula, the first line makes the function loop until the outcome is 1 which in theory should always return 4 which becomes 2 which then becomes 1 creating an infinite loop
![Function](https://cdn.discordapp.com/attachments/875826551571222538/1025400304071610378/unknown.png)
### Then we have two checks for whether the number is odd or even to which it applies the correct formula and prints the outcome
![Function pt 2](https://cdn.discordapp.com/attachments/875826551571222538/1025400705059667999/unknown.png)
### At last we call upon the function to actually run the conjecture
![Calling funtion](https://cdn.discordapp.com/attachments/875826551571222538/1025400951718297661/unknown.png)
## About the script
### Im learning python and I think that this would be useful for anyone that is trying to replicate the conjecture.
### Im also obsessed with this problem, im also working on randint solver so it creates random numbers for the conjecture.

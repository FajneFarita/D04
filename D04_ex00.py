#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random


# Body

def guess_the_num():
    arbitrary_number = random.randint(1, 25)
    count = 1
    while count <= 5:
        try:
            guess = int(input('Guess the integer number from 1 to 25. You have 5 tries: '))
            
        except ValueError:
            print("Seems like it's not a valid input. Try again")
            count +=1
            continue
        if guess in range(1, 26):
            if guess == arbitrary_number:
                print("Correct!")
                break
            elif guess < arbitrary_number:
                print("Too low")
                count +=1
            else:
                print("Too high")
                count +=1
        else:
            print("Seems like it's not in range. Try again")
            count +=1
            continue




################################################################################
def main():


    guess_the_num() # Remove this and replace with your function calls


if __name__ == '__main__':
    main()

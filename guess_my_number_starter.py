"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
#This is use to generate random numbers
import random

#Variable set to random numbers generated
my_guess = random.randint(1, 99)
print("I am thinking of a number between 1 and 99")

#Takes input from the user and converts it to an interger.
user_num = int(input('Enter a guess: '))

#This checks if the users input is equal to the random number generated
while (user_num != my_guess):

#The if condition checks whether the user's guess is less or higher than the secret number
    if user_num < my_guess:
        print('Your guess is too low')
         = int(input('Enter a guess: '))
    elif user_num >my_guess:
        print('Your guess is too high')
        user_num = int(input('Enter a guess: '))

#what prints when user gets it correct
else:
    print("Congrats! The number was: " ,user_num)

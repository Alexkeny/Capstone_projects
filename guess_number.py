# Guess game
# In this game you need to guess randomly generated number.
# You can enter boundary to extend range of the randomly generated number.
# What you need to know to programm this game: variables, int(), input(), print(),
# while, break, continue, random module (.randint()), .isdigit()

import random

def is_valid(n, boundary):
    '''Checking user input. Return True if user input is a number 
    from 1 to user defined boundary and False otherwise.'''
    return n.isdigit() and (0 < int(n) <= boundary)

def boundary_check():
    '''User is input new boundary for random function'''
    while True:
        n = input("Please enter boundary. It must be number from 10 to 1000: ")
        if n.isdigit() and (10 < int(n) <= 1000):
            return int(n)
        else:
            print("Incorrect input")
            continue


def generate_random_num(bound):
    '''This function will generate random number'''
    return random.randint(1, bound)

flag = True

print("Welcome to the game! Guess the number.")

while flag:
    boundary = boundary_check()
    count = 0
    random_number = generate_random_num(boundary)
    while True:
        guess = input(f"Please enter number from 1 to {boundary}: ")
        if is_valid(guess, boundary):
            guess = int(guess)
            if guess < random_number:
                print("Your guess is less then number.")
                count += 1
                continue
            elif guess > random_number:
                print("Your guess is higher then number.")
                count += 1
                continue
            elif guess == random_number:
                print(f"You win! Number of attemps is {count}")
                one_more_time = input("Would you like to play one more time? y/n ")
                if one_more_time == 'y':
                    break
                else:
                    flag = False
                    break
        else:
            print(f"There must be number from 1 to {boundary}.")
            continue

print("Thanks for playing!")

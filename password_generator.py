# Simple password generator based on random module
# for learning purposes only

import random

digits = '01234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!#$%&*+-=?@^_'
excluded = 'il1Lo0O '

chars = '' # to store our password 
# CAUTION it's unsave to store password in plaintext

def check_num():
    '''Validates numeric user input'''
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        else:
            print("Print a number")

def check_char():
    '''Validates (y/n) user input and return True if y and False if n'''
    while True:
        char = input()
        if char.isalpha() and char in ('y', 'n'):
            if char == 'y':
                return True
            elif char == 'n':
                return False
            else:
                continue
        else:
            print('Please enter y or n')

def pass_num():
    '''Take numer of passwords from user and validate input'''
    print("How much passwords do you need?")
    return check_num()

def pass_len():
    '''Take a length of the pass and validate input'''
    print("How long password should be? It's recommended to use at least 16: ")
    return check_num()

def include_num():
    print("Do you wish to include numbers? It's recommended, choose (y/n): ")
    return check_char()

def include_upper():
    print("Do you wish to include upper case letter? It's recommended, choose (y/n): ")
    return check_char()

def include_lower():
    print("Do you wish to include lower case letter? It's recommended, choose (y/n): ")
    return check_char()

def include_special():
    print("Do you wish to include special symbols? It's recommended, choose (y/n): ")
    return check_char()

def exclude_some():
    print("Do you wish to exclude symbols: il1Lo0O ? Usually people make mistakes in password because of it choose (y/n): ")
    return check_char()

def generate_password(pass_length, chars_list):
    print('Your password is')
    for _ in range(pass_length):
        print(random.choice(chars_list), end='')
    print()

while True:
    password_num = pass_num()
    password_len = pass_len()
    password_nums = include_num()
    password_up = include_upper()
    password_low = include_lower()
    password_spec = include_special()
    password_some = exclude_some()

    if password_nums:
        chars += digits
    if password_up:
        chars += uppercase_letters
    if password_low:
        chars += lowercase_letters
    if password_spec:
        chars += special
    if password_some:
        for c in excluded:
            chars = chars.replace(c, '')

    if len(chars) != 0:
        for _ in range(password_num):
            generate_password(password_len, chars)
        break
    else:
        print('There is no options for password. Choose at least one. Try one more time? (y/n)')
        if check_char():
            continue
        else:
            break
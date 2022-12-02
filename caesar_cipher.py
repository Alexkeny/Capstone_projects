# Caesar Cipher it's a simple encryption algorithm.
# In this task we're using EN and RU alphbet.

# TO-DO
# 1. User input: encript or decript
# 2. Alphabet EN (26 symbols) or RU (32 symbols)
# 3. Rotation
# 4. Upper and lower case must be on their places, punctuation is not changed

# Alphabet samples
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Functions
def choose_language():
    '''Asks user about alphabet. Take user input, validate it and return 'en' or 'ru' string'''
    while True:
        cipher_language = input('What language would you like to use? (en/ru)')
        if cipher_language == 'en':
            return 'en'
        elif cipher_language == 'ru':
            return 'ru'
        else:
            print("Incorrect input. Please provide en (for English) or ru (for Russian)")

def choose_encription():
    '''Asks user about two options: encrypt or decript. Take user input, validate it 
    and return 'enc' or 'dec' string'''
    while True:
        encr_decr = input('Would you like encrypt (e) or decript (d)? (e/d) ')
        if encr_decr == 'e':
            return 'enc'
        elif encr_decr == 'd':
            return 'dec'
        else:
            print("Incorrect input. Please provide e (for encription) or d (for decription)")

def choose_rotate(language):
    '''Asks user about rotate number and validate input. 
    For en is from 1 to 26, for ru is from 1 to 32.
    Function must use two arguments: language (en/ru) and encrypt (enc or decr)'''
    while True:
        if language == 'en':
            rotate = input(f"Input rotation for English. It should be from 1 to {len(eng_lower_alphabet)}: ")
            if 0 < int(rotate) < 26:
                return int(rotate)
            else:
                print(f"Incorrect number. It should be up to {len(eng_lower_alphabet)}.")
                continue
        elif language == 'ru':
            rotate = input(f"Input rotation for Russian. It should be from 1 to {len(ru_lower_alphabet)}: ")
            if  1 < int(rotate) < 32:
                return int(rotate)
            else:
                print(f"Incorrect number. It should be up to {len(ru_lower_alphabet)}.")

def encrypt(text, rotate, lang):
    '''This function accepts text, rotate and lang arguments and perform text encryption.'''
    encrypted_text = ''

    if lang == 'en':
        for c in text:
            if c in eng_lower_alphabet:
                if (ord(c) + rotate) > 122:
                    encrypted_text += chr((ord(c) + rotate) - 26)
                elif (ord(c) + rotate) <= 122:
                    encrypted_text += chr(ord(c) + rotate)
            elif c in eng_upper_alphabet:
                if (ord(c) + rotate) > 90:
                    encrypted_text += chr((ord(c) + rotate) - 26)
                elif (ord(c) + rotate) <= 90:
                    encrypted_text += chr(ord(c) + rotate)
            else:
                encrypted_text += c
    else:
        for c in text:
            if c in ru_lower_alphabet:
                if (ord(c) + rotate) > 1103:
                    encrypted_text += chr((ord(c) + rotate) - 32)
                elif (ord(c) + rotate) <= 1103:
                    encrypted_text += chr(ord(c) + rotate)
            elif c in ru_upper_alphabet:
                if (ord(c) + rotate) > 1071:
                    encrypted_text += chr((ord(c) + rotate) - 32)
                elif (ord(c) + rotate) <= 1071:
                    encrypted_text += chr(ord(c) + rotate)
            else:
                encrypted_text += c
    
    return encrypted_text

def decrypt(text, rotate, lang):
    '''This function accepts text, rotate and lang arguments and perform text decryption.'''
    decrypted_text = ''

    if lang == 'en' and ord(text[0]) < 123:
        for c in text:
            if c in eng_lower_alphabet:
                if (ord(c) - rotate) >= 97:
                    decrypted_text += chr(ord(c) - rotate)
                elif (ord(c) - rotate) < 97:
                    decrypted_text += chr(ord(c) - rotate + 26)
            elif c in eng_upper_alphabet:
                if (ord(c) - rotate) >= 65:
                    decrypted_text += chr(ord(c) - rotate)
                elif (ord(c) - rotate) < 65:
                    decrypted_text += chr(ord(c) - rotate + 26)
            else:
                decrypted_text += c
    elif lang == 'ru' and 1008 < ord(text[0]) < 1104:
        for c in text:
            if c in ru_lower_alphabet:
                if (ord(c) - rotate) < 1072:
                    decrypted_text += chr((ord(c) - rotate) + 32)
                elif (ord(c) - rotate) >= 1072:
                    decrypted_text += chr(ord(c) - rotate)
            elif c in ru_upper_alphabet:
                if (ord(c) - rotate) < 1040:
                    decrypted_text += chr(ord(c) - rotate + 32)
                elif (ord(c) - rotate) >= 1040:
                    decrypted_text += chr(ord(c) - rotate)
            else:
                decrypted_text += c
    else:
        print("Oops. Language and input text language is different. Try to start programm one more time.")
    return decrypted_text


# Main programm
print("Welcome to Caesar Cipher")
text = input("Put your text: ")
lang = choose_language()
rotate = choose_rotate(lang)

if choose_encription() == 'dec':
    print(decrypt(text, rotate, lang))
else:
    print(encrypt(text, rotate, lang))


# Additional task
# take user input, rotate for each word is the length of the word (wothout special symbols)
""" text = input().split()
print(text)
result = ''
for item in text:
    special = ''
    count = 0
    if item.isalpha():
        result = result + ' ' + encrypt(item, len(item), 'en')
    else:
        for char in item:
            if char.isalpha():
                count += 1
        for char in item:
            if char.isalpha():
                special += encrypt(char, count, 'en')
            else:
                special += char
        result = result + ' ' + special
print(result) """
# Hangman game
# player should guess the word

import random
word_list = ['funny', 'matrix','jelly','scratch', 'crypt', 'oxygen','unzip', 'subway', 'cycle', 
'icebox', 'wave', 'zombie']

def get_word():
    '''Return random word from the list in the upper register'''
    return random.choice(word_list)

def display_hangman(tries):
    '''Acceps number of tries and print current state'''
    stages = [  # final state
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, body, arms, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, body, two arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, body, one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head, body
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # start
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    '''Main game and logic. As an argument use return of the get_word() func'''

    word_completion = '_' * len(word)  # symblos for each letter of the word
    guessed = False                    # flag
    guessed_letters = []               # guessed letterss
    guessed_words = []                 # list of the already guessed words
    tries = 6                          # try

    print("Let's play Hangman")
    print(display_hangman(tries))
    print("Word:", word_completion)
    print(word)
    
    while True:
        guess = input(f"Provide your guess word or letter. Word has {len(word)} letters: ")
        word_completion = ''
        if guess.isalpha():    # validate user input
            if len(guess) == 1:
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
                    if guess in word:
                        for i in range(len(word)):
                            if word[i] in guessed_letters:
                                word_completion += word[i]
                                print(word[i], end='')
                            else:
                                word_completion += '_'
                                print('_', end = '')
                        print()
                        print("Nice, you guess letter ")
                        if word_completion == word:
                            print("and the word")
                            guessed = True
                            break
                        continue
                    else:
                        print(f'There is no such letter in the word. You have {tries} tries')
                        tries -= 1
                        print(display_hangman(tries))
                        if tries == 0:
                            break
                        print(f"You have {tries}")
                        continue
                else:
                    print('You already choosed this letter. Try another.')
                    continue
            elif len(guess) == len(word):
                if guess == word:
                    guessed = True
                    break
                if guess not in guessed_words:
                    guessed_words.append(guess)
                    tries -= 1
                    if tries == 0:
                        break
                    print(f'Incorrect word. You have {tries}')
                    continue
                else:
                    print('You already choosed this word. Try another.')
                    continue
            else:
                print(f'Incorrent number of letters. It should be one letter or word with {len(word)} letters.')
                continue
        else:
            print("Incorrect symbol.")
            break # REPLACE TO CONTINUE BEFORE PRODUCTION
    
    if guessed and (tries > 0):
        return print('Congratulations!')
    else:
        return print("Game is over.")


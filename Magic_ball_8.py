# Magic ball 8 game
# Game has 20 possible answers

import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
'Concentrate and ask again', "Don’t count on it", 'My reply is no', 'My sources say no',
'Outlook not so good', 'Very doubtful']

print("Hello World! I'm magic ball and know all the answers.")
name = input("What is your name? ")
print(f'Hello {name}')

while True:
    question = input("What is your question? ")
    print(random.choice(answers))
    question = input("Do you have another questions? y/n ")
    if question == 'y':
        continue
    else:
        break
print(f'Will see you later, {name}')
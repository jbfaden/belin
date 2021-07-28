import random

print("I'm thinking of a number between 1 and 100.  Can you guess it?")

number = random.randint(0, 10)

guess = int(input('what is your guess? '))

while guess != number:
    if guess < number:
        print('higher...')
    else:
        print('lower...')
    guess = int(input('what is your guess? '))

print('You got it!')

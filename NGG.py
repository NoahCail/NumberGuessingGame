'''Python program for a small number guessing game'''

import random as r

#Intro Screen Loadout

logo = '''
  _____                   __  __         _  __           __          
 / ___/_ _____ ___ ___   / /_/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<  / __/ _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/  \__/_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   
'''

NUMBERS = list(range(101))

def game_intro(random_number):
    '''Initializes the game'''

    print(logo)

    print('Welcome to the Number Guessing Game! \n I am thinking of a number between 0 and 100, can you guess it?')

    difficulty = input('Please select a difficulty by either typing \'Easy\' or \'Hard\' here: ')

    if difficulty == 'Easy':
        print('You have 10 guesses remaining')
        guess_input(10, r.choice(NUMBERS))
    elif difficulty == 'Hard':
        print('You have 5 guesses remaining')
        guess_input(5, r.choice(NUMBERS))
    else:
        print('Please only type in \'Easy\' or \'Hard\'')
        #Need to figure out how to clear the console here
        game_intro(r.choice(NUMBERS))

def play_again(reply):
    '''Restarts the game if the user wants to play again'''
    
    if reply == 'Yes':
        game_intro(r.choice(NUMBERS))
    elif reply == 'No':
        print('Thanks for playing!')

def guess_input(guesses, correct_number):
    
    while guesses > 0:

        guess = int(input('Make your guess here: '))

        try:
            if guess == correct_number:
                print(f'You got it! The number was {correct_number}')
                answer = input('Would you like to play again? Type \'Yes\' or \'No\':')
                play_again(answer)
                guesses = 0
            elif guess > correct_number:
                print('Too high. Guess again below')
                guesses -= 1
                print(f'Guesses Remaining: {guesses}')
                guess_input(guesses, correct_number)
            elif guess < correct_number:
                print('Too low. Guess again below')
                guesses -= 1
                print(f'Guesses Remaining: {guesses}')
                guess_input(guesses, correct_number)
        except:
            print('Please enter a valid number between 0 and 100')
            guess_input(guesses, correct_number)

    else:
        print('You ran out of guesses. You lose.')
        answer = input('Would you like to play again? Type \'Yes\' or \'No\':')
        play_again(answer)


game_intro(r.choice(NUMBERS))
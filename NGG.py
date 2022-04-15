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

def clearConsole():
    print('\n' * 150)

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
        clearConsole()
        game_intro(r.choice(NUMBERS))
    elif reply == 'No':
        print('Thanks for playing!')
    else:
        print(f'Please only type \'Yes\' or \'No\' below')
        answer = input('Would you like to play again? Type \'Yes\' or \'No\': ')
        play_again(answer)

def guess_input(guesses, correct_number):
    '''Asks the user for a number and checks to see if it is correct, too high, or too low'''
    
    if guesses == 0 or guesses < 0:
        print(f'You ran out of guesses. You lose. \n The number was {correct_number}.')
        answer = input('Would you like to play again? Type \'Yes\' or \'No\': ')
        play_again(answer)

    else:

        guess = int(input('Make your guess here: '))

        if guess == correct_number:
            print(f'You got it! The number was {correct_number}!')
            answer = input('Would you like to play again? Type \'Yes\' or \'No\': ')
            play_again(answer)

        while guess != correct_number and guesses > 0 and hope:

                try:
                    if guess > correct_number:
                        guesses -= 1
                        if guesses == 0:
                            print('Sorry, too high.')
                            guess_input(guesses, correct_number)
                        else:
                            print('Too high. Guess again below')
                            print(f'Guesses Remaining: {guesses}')
                            guess_input(guesses, correct_number)
                    elif guess < correct_number:
                        guesses -= 1
                        if guesses == 0:
                            print('Sorry, too low.')
                            guess_input(guesses, correct_number)
                        else:
                            print(f'Guesses Remaining: {guesses}')
                            print('Too low. Guess again below')
                            guess_input(guesses, correct_number)
                except:
                    print('Please enter a valid number between 0 and 100')
                    guess_input(guesses, correct_number)

game_intro(r.choice(NUMBERS))
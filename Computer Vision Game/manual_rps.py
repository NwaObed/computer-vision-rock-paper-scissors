import random


options = ['rock', 'paper', 'scissors']


def get_computer_choice():
    return random.choice(options)

def get_user_choice():
    print('Your available choices are : rock, paper, scissors')
    while True:
        player_choice = input('Please enter your choice : ')
        if player_choice.lower() in options:
            break
        else:
            print('Your choice is invalid. Please enter one of the available choices')
    return player_choice

# computer_choice = get_computer_choice()
# user_choice = get_user_choice()

def get_winner(computer_choice, user_choice):
    #convert the choices to lowercases
    computer_choice = computer_choice.lower()
    user_choice = user_choice.lower()

    if computer_choice == user_choice:
        print('It is a tie')
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print('You lost')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print('You lost')
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('You lost')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You won')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You won')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You won')

def play():

    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        get_winner(computer_choice, user_choice)
    
play()
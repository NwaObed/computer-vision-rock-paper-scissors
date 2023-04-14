import random


options = ['rock', 'paper', 'scissors']


class RPS:
    def __init__(self, num_of_rounds = 5):
        self.num_of_rounds = num_of_rounds

    def get_computer_choice(self):
        return random.choice(options)

    def get_user_choice(self):
        print('Your available choices are : rock, paper, scissors')
        while True:
            player_choice = input('Please enter your choice : ')
            if player_choice.lower() in options:
                break
            else:
                print('Your choice is invalid. Please enter one of the available choices')
        return player_choice

    def get_winner(self, computer_choice, user_choice):
        #convert the user choice to lowercases
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

    def play(self):
        number_of_rounds = self.start_game()
        while number_of_rounds > 0:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()
            self.get_winner(computer_choice, user_choice)
            number_of_rounds -= 1
            if number_of_rounds == 0:
                print('The round has ended. Do you wish to continue? (y/n)')
                user_decision = input().lower()
                if user_decision == 'y':
                    number_of_rounds = self.start_game() #reset the number of rounds
                elif user_decision == 'n':
                    print('Thank you for playing! The game is over now.')

    def start_game(self):
        number_of_rounds = self.num_of_rounds
        return number_of_rounds

rps = RPS(3)
rps.play()

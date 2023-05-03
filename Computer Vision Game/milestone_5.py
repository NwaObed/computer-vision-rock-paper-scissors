import random
import time
import numpy as np
import cv2
from keras.models import load_model



model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

with open('labels.txt', 'r') as myfile:
    labels = [line.strip().split()[1] for line in myfile]
class Rps:
    '''
    This class implements the rock-paper-scissors game between a single user and 
    the computer

    Attributes:
    computer_wins (int) : number of wins by the computer. (default :0)
    user_wins (int)     : number of wins by the user. (default :0)
    rounds (int)        : number of rounds until either computer or user wins (default :3)
    '''
    def __init__(self, computer_wins=0, user_wins=0, rounds=3):
        self.computer_wins = computer_wins
        self.user_wins = user_wins
        self.rounds = rounds
    
    def capture_image(self):
        'This function captures the image of the objects'
        return cv2.VideoCapture(0)
    
    def resize_image(self,cap):
        '''
        This function normalize the image sizes

        Arg:
        cap : Image of the object captured from camera

        Return:
        It returns the normalized image
        '''
        #Read or capture the objects from camera in real time
        ret, frame = cap.read()
        #Resize the captured images
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        #Normalize the image to values between 0 and 1
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        return data, frame
    def countdown_timer(self, cap):
        '''
        The function prints the timer before object image is captured on the user's screen 
        
        Arg:
        cap : Image of the object captured from camera
        '''
        start_time = time.time()
        while time.time() - start_time <= 5: 
            time_counter = 5 - int(time.time() - start_time)
            frame = self.resize_image(cap)[1]
            if time_counter == 2:
                #print the timer on screen
                frame = cv2.putText(frame, 'GO!', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            elif time_counter == 1:
                frame = cv2.putText(frame, '', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            else:
                frame = cv2.putText(frame, str(time_counter-2), (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def get_prediction(self, cap):
        '''
        This function predicts the object captured from the camera using a pretrained
        model from trainable machines. It prints the user object on the screen using OpenCV module

        Arg:
        cap : normalized image of the object captured from the camera after the countdown
        '''
        data, frame = self.resize_image(cap)
        # predict the user object using the pretrained model
        prediction = model.predict(data)
        p = np.argmax(prediction)
        #labels = self.label()
        #print(f'You chose {labels[p]}')
        frame = self.resize_image(cap)#
        cv2.putText(frame, 'Your chose', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
        cv2.imshow('frame', frame)
        return labels[p]#.split()[1]

    def __track_wins(self,winner='user'):
        '''
        This function keeps track of the scoreboard
        
        Args:
        winner (str) : Default value is 'user'
        '''
        if winner == 'computer':
            self.computer_wins += 1
            print('You lost')
        else:
            self.user_wins += 1
            print('You won')



    def get_winner(self, computer_choice, user_choice):
        '''
        This function decides the winner of the game using the classic rules of RPS game.

        Arg:
        computer_choice (str) : Random choice of the computer. Values are 'rock', 'paper', 'scissors'
        user_choice (str) : The user's choice from _get_prediction() function.
        '''
        count_computer_wins = self.computer_wins
        count_user_wins = self.user_wins
        computer_choice = computer_choice.lower()
        user_choice = user_choice.lower()

        if computer_choice == user_choice:
            print('It is a tie')
        elif computer_choice == 'rock' and user_choice == 'scissors':
            self.__track_wins('computer')
        elif computer_choice == 'scissors' and user_choice == 'paper':
            self.__track_wins('computer')
        elif computer_choice == 'paper' and user_choice == 'rock':
            self.__track_wins('computer')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            self.__track_wins()
        elif user_choice == 'scissors' and computer_choice == 'paper':
            self.__track_wins()
        elif user_choice == 'paper' and computer_choice == 'rock':
            self.__track_wins()


    def play(self):
        'This function plays the Rps game until the computer or the user wins a round'
        while True:
            print(self.user_wins,self.computer_wins)
            if self.computer_wins == 3 or self.user_wins == 3:
                print('The round has ended. Do you wish to continue? (y/n)')
                user_decision = input().lower()
                if user_decision == 'y':
                    self.computer_wins =0
                    self.user_wins = 0
                elif user_decision == 'n':
                    print('Thank you for playing! The game is over now.')
                    break
            cap = self.capture_image()
            user_choice = self.get_prediction(cap)
            computer_choice = random.choice(labels)
            print(user_choice)
            print(computer_choice)
            winner = self.get_winner(computer_choice, user_choice)
            #print(computer_wins, user_wins)
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()
        


rps = Rps()

rps.play()
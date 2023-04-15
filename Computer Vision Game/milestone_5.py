import random
import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

with open('labels.txt', 'r') as myfile:
    labels = [line.strip().split()[1] for line in myfile]
computer_wins = 0
user_wins = 0
class RPS:
    def __init__(self, computer_wins=0, user_wins=0):
        self.computer_wins = computer_wins
        self.user_wins = user_wins
    
    def capture_image(self):
        return cv2.VideoCapture(0)
    
    def get_predictiion(self, cap):
        start_time = time.time()
        #count_down = 3
        while time.time()  < start_time+5: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            if time.time() <= start_time+1:
                frame = cv2.putText(frame, '3', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            elif time.time() <= start_time+2:
                frame = cv2.putText(frame, '2', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            elif time.time() <= start_time+3:
                frame = cv2.putText(frame, '1', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            elif time.time() <= start_time+4:
                frame = cv2.putText(frame, 'GO!', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            else:
                frame = cv2.putText(frame, '', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
            prediction = model.predict(data)
            #count_down += 1
            cv2.imshow('frame', frame)
            # Press q to close the window
            #print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            #elif int(time.time()) == int(start_time + 5):
        p = np.argmax(prediction)
        #labels = self.label()
        print(f'You chose {labels[p]}')
        
        return labels[p]#.split()[1]

    
    def get_winner(self, computer_choice, user_choice):
        #convert the choices to lowercases
        count_computer_wins = self.computer_wins
        count_user_wins = self.user_wins
        computer_choice = computer_choice.lower()
        user_choice = user_choice.lower()

        if computer_choice == user_choice:
            print('It is a tie')
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print('You lost')
            self.computer_wins += 1
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print('You lost')
            self.computer_wins += 1
        elif computer_choice == 'paper' and user_choice == 'rock':
            print('You lost')
            self.computer_wins += 1
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('You won')
            self.user_wins += 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('You won')
            self.user_wins += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You won')
            self.user_wins += 1


    def play(self):
        while True:
            print(self.user_wins,self.computer_wins)
            if self.computer_wins == 3 or self.user_wins == 3:
                print('The round has ended. Do you wish to continue? (y/n)')
                user_decision = input().lower()
                if user_decision == 'y':
                    self.computer_wins, self.user_wins = self.reset_game() #reset the scoreboard
                elif user_decision == 'n':
                    print('Thank you for playing! The game is over now.')
                    break
            cap = self.capture_image()
            user_choice = self.get_predictiion(cap)
            computer_choice = random.choice(labels)
            print(user_choice)
            print(computer_choice)
            winner = self.get_winner(computer_choice, user_choice)
            #print(computer_wins, user_wins)
            # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

    def reset_game(self):
        reset_computer_count = 0
        reset_user_count = 0
        return reset_computer_count, reset_user_count
        


rps = RPS()

rps.play()
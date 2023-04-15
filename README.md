# Computer Vision RPS

## Milestone 1
The image model used in this project is trained using images of my hand with closed fist as ```rock```, a fist with two fingers out as ```scissors``` and open palm as ```paper```. An image of these three objects are recorded and used to train the model which can predict the objects when shown to the camera. I am going to use the model to play the popular ```rock-paper-scissors game```. My goal is for the model to predict the users and choice and play with the computer using the classic rules of the game.

## Milestone 4
In this milestone, the user selects one of the the three objects -- ```rock, paper``` or ```scissors```. Similarly, the computer randomly picks one the objects and the winner is picked using the following code snippets:

```python
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
```

##Milestone 5
In this final milestone, I implemented the RPS ```class``` initiating the value of two class variables ```computer_wins``` and ```user_wins``` that keeps records of the game scoreboard. When a player wins three rounds, the round ends and the player can chose to end the game or continue. The game can reset using the following code:

```python
if self.computer_wins == 3 or self.user_wins == 3:
    print('The round has ended. Do you wish to continue? (y/n)')
    user_decision = input().lower()
    if user_decision == 'y':
        self.computer_wins, self.user_wins = self.reset_game() #reset the scoreboard
    elif user_decision == 'n':
        print('Thank you for playing! The game is over now.')
        break
```

To start the game, the image model created and trained in ```Milestone 1```, predicts the players choice and the competes with the computer's random choice. Before the model predicts the player's model, a countdown of ```3-2-1-GO!``` shows on the players screen. 

```python
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
```

To decide the winner of each show, the classic rule of the game is followed as shown on the code:

```python
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
```
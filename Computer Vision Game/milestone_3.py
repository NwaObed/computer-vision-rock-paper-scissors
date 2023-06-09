import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

start_time = int(time.time())
with open('labels.txt', 'r') as myfile:
    labels = [line.strip() for line in myfile]
while int(time.time())  <= start_time+5: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif int(time.time()) == start_time + 5:
            p = np.argmax(prediction)
            print(f'You chose {labels[p].split()[1]}')
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
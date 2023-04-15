import cv2
import numpy as np
from datetime import datetime


data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
cap = cv2.VideoCapture(0)

# Initialize variables
camSource = -1
running = True
saveCount = 0
nSecond = 0
totalSec = 3
strSec = '9876543210'
keyPressTime = 0.0
startTime = 0.0
timeElapsed = 0.0
startCounter = False
endCounter = False

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    #prediction = model.predict(data)
    print(nSecond)
    if nSecond < totalSec:
        strS = strSec[nSecond]
    frame = cv2.putText(frame, 'OK', (200, 250),cv2.FONT_HERSHEY_DUPLEX,5,(256,0,0))
    cv2.imshow('frame', frame)
    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    nSecond += 1

            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
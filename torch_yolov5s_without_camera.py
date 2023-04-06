import cv2, torch, time
import numpy as np
from playsound import playsound
import random

voices = ['angry-kitty.wav', 'cat-roar.wav', 'dog-barking.wav', 'eagle.wav']


# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

stream = cv2.VideoCapture(0)
while True:
    ret, frame = stream.read()
    results = model([frame])
    labels = results.pandas().xyxy[0]['name'].tolist()
    if 'person' in labels:
      results.save()
      time.sleep(0.5)
      voice = random.choice(voices)
      print(voice)
      playsound('voices/' + voice)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()

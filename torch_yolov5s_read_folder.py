import cv2, torch, time
import numpy as np
from glob import glob

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

DIRECTORY = '/home/haiyang/Downloads/ExDark/all/'

image_list = []
files = glob(DIRECTORY + '*.jpeg')
files.extend(glob(DIRECTORY + '*.png'))
files.extend(glob(DIRECTORY + '*.jpg'))

for filename in files:
    results = model([filename])
    labels = results.pandas().xyxy[0]['name'].tolist()
    if 'bird' in labels:
      results.save()
      print(labels)
    cv2.namedWindow('yolov5', cv2.WINDOW_NORMAL)
    cv2.imshow('yolov5', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

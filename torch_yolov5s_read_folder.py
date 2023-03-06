import cv2, torch, time
import numpy as np
from glob import glob

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

DIRECTORY = 'YOUR-IMAGE-FOLDER'

image_list = []
files = glob(DIRECTORY + '*.jpeg')
files.extend(glob(DIRECTORY + '*.png'))
files.extend(glob(DIRECTORY + '*.jpg'))

for filename in files:
    results = model([filename])
    print(results.pandas().xyxy[0]['name'].tolist())
    cv2.namedWindow('yolov5', cv2.WINDOW_NORMAL)
    cv2.imshow('yolov5', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(2)

cv2.destroyAllWindows()

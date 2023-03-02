import cv2, torch, time
import numpy as np
import glob

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

DIRECTORY = 'YOUR-IMAGE-FOLDER'

image_list = []
for filename in glob.glob(DIRECTORY + '*.png'):
    print(filename)
    results = model([filename])
    print(results)
    cv2.imshow('Video Stream Monitor', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cv2.destroyAllWindows()

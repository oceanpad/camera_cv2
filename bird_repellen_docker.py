import cv2, torch, time, logging
import numpy as np

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

stream = cv2.VideoCapture(0)
while True:
    ret, frame = stream.read()
    results = model([frame])
    labels = results.pandas().xyxy[0]['name'].tolist()
    logging.info(labels)
    if 'bird' in labels:
      results.save()
      print(labels)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.5)

stream.release()
cv2.destroyAllWindows()


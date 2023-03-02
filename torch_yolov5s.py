import cv2, torch, time
import numpy as np

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

stream = cv2.VideoCapture(0)
while True:
    ret, frame = stream.read()
    # frame = cv2.flip(frame, 0)
    results = model([frame])
    cv2.imshow('Video Stream Monitor', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

stream.release()
cv2.destroyAllWindows()

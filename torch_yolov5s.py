import cv2, torch, time
import numpy as np

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

stream = cv2.VideoCapture(0)
while True:
    ret, frame = stream.read()
    # frame = cv2.flip(frame, 0)
    results = model([frame])
    labels = results.pandas().xyxy[0]['name'].tolist()
    if 'person' in labels:
      results.save()
      print(labels)

    cv2.imshow('Video Stream Monitor', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()

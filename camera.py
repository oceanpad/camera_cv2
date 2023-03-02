import cv2

stream = cv2.VideoCapture(0)

while True:
    ret, frame = stream.read()
    image = cv2.flip(frame, 0)
    cv2.imshow('Video Stream Monitor', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
stream.release()
cv2.destroyAllWindows()

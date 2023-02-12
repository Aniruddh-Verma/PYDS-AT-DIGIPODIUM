import cv2 
video = cv2.VideoCapture(0)

while True:
      status, img = video.read()
      if not status:
            break
      cv2.imshow('video',img)
      if cv2.waitKey(1) == 27:
            break
video.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

video = cv2.VideoCapture(0)

image = cv2.imread("temple.jpg")


while(video.isOpened()):
   
    ret, frame = video.read()

    
    image = cv2.resize(image, (640, 480))
    frame = cv2.resize(frame, (640,480))

    
    u_black = np.array([100,153,70])
    l_black = np.array([30,30,0])

    
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    f = frame - res
    
    f = np.where(f == 0, image, f)

    final_output = cv2.addWeighted(f, 1, image, 0, 0)

    cv2.imshow("MY PHOTOS IN BANGKOK...", final_output)
    key = cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()

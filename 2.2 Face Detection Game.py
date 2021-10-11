import cv2
import numpy as np

video = cv2.VideoCapture(0) #Capturing video feed from the WebCam
video.set(3, 640) #Setting width to 640
video.set(4, 480) #Setting height to 480

img = np.zeros((480, 640, 3), np.uint8) #Creating a new image using numpy library
img[:] = 136, 255, 168 #Setting colour for image

i = 0
a = 0
b = 0
vx = 0
vy = 0

fcasc = cv2.CascadeClassifier(r"C:\Users\shroy\PycharmProjects\ARK\Resources/haarcascade_frontalface_default.xml")

while True:
    success, frame = video.read()
    framegs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gameface = fcasc.detectMultiScale(framegs, 1.1, 4)

    for (x, y, w, h) in gameface:
        radius = (int)((w + h) / 4) + 2
        cx = (int)(x + radius)
        cy = (int)(y + radius)
        center = (cx, cy)
        cv2.circle(frame, (cx, cy), radius, (255, 255, 255), 1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "PRESS 'q' TO ESCAPE", (0, 35), font, 1, (255, 0, 0), 2, cv2.LINE_4)

    cv2.circle(img, ((320+a),(240+b)), 50, (255, 255, 255), -1)
    cv2.circle(img, (640, 400), 80, (0, 0, 0), -1)

    cv2.imshow("Image", img)
    cv2.waitKey(2)

    cv2.imshow("Video", frame)

    cv2.circle(img, ((320+a),(240+b), 50, (136, 255, 168), -1)
    cv2.circle(img, (640, 400), 80, (136, 255, 168), -1)

    j = ((320-cx-x)*(320-cx-x))
    l = ((160-y)*(160-y))

    if (j + l)!=16900:
        if i==0:
            b = b + 1

        else:
            a = a + vx
            b = b - vy


    if (j + l)==16900:
        i = i + 1
        if j<=l:
            vx = 3
            vy = (int)((160 - y) / (320 - cx - x)) * vx

        else:
            vy = 3
            vx = (int)((320 - cx - x)/(160 - y)) * vy

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

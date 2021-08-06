import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('FRIENDS.jpg')
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#print(face_coordinates)

#[[352 135 474 474]]
#cv2.rectangle(img, (352, 135), (352+474, 135+474), (0, 255, 0), 10)

# Drow Recabgle In single face image
#(x, y, w, h) = face_coordinates[0]
#cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 10)

# multiple images
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 10)


# cv2.imshow('Clever Programmer', img)
# cv2.waitKey()


webcam = cv2.VideoCapture(0) # 0 for default webcam
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 10)
    cv2.imshow('Clever Programmer', frame)
    key = cv2.waitKey(1)
    if key == 81 or key== 113:
        break



webcam.release()


print('Code Completed')
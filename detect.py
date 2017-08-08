import sys
import os
import cv2

if __name__ == '__main__':
    img = cv2.imread('./timg.jpeg')
    cv2.imshow('image', img)

    current_dir = os.path.dirname(os.path.realpath(__file__))
    xml_path = os.path.join(current_dir, './model/haarcascade_frontalface_alt2.xml')
    face_detector = cv2.CascadeClassifier(xml_path)    
    faces_rect = face_detector.detectMultiScale(img, scaleFactor=1.2, minNeighbors=2, flags=0, minSize=(60, 60))
    print ("faces count: %d"%(len(faces_rect)))
    if len(faces_rect)>0:
        for faceRect in faces_rect:
            x, y, w, h=faceRect
            cv2.circle(img, (x+w/2,y+h/2), min(w/2,h/2), (255,0,0))
    cv2.imwrite('face.png', img)
    cv2.imshow("image", img) 
    cv2.waitKey(0)
        
   
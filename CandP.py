

import cv2

#img = 'C:/Users/Vishan/OneDrive/Desktop/CarAndPedestrian/carimg.png'
video = cv2.VideoCapture('C:/Users/Vishan/OneDrive/Desktop/AI projects/CarAndPedestrian/mix.mp4')
frame_width = int(video.get(3))
frame_height = int(video.get(4))
   
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    

#pretrained car classifier
car_tracker_file = 'C:/Users/Vishan/OneDrive/Desktop/AI projects/CarAndPedestrian/car_detector2.xml'
ped_tracker_file = 'C:/Users/Vishan/OneDrive/Desktop/AI projects/CarAndPedestrian/haarcascade_fullbody.xml'

#making the car classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)
ped_tracker = cv2.CascadeClassifier(ped_tracker_file)

#Loop to run video
while True:
    (read_successful,frame) = video.read()

    if read_successful:
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        result.write(frame)
    else:
        break

    cars = car_tracker.detectMultiScale(gray_frame)
    peds = ped_tracker.detectMultiScale(gray_frame)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.rectangle(frame ,(x+1,y+2),(x+w,y+h),(255,0,0),2)

    for(x,y,w,h) in peds:
        cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,255,255),2)

    
    cv2.imshow('Autodrive', frame)
    key = cv2.waitKey(1)
    #Break out of loop if q entered
    if key==81 or key == 113:
        break

video.release()

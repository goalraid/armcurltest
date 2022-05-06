
from pynput.keyboard import Key, Controller


# In[5]:

import time
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# In[6]:    

import serial

import time

servo = serial.Serial('COM6', 9600)

servo.timeout = 1

keyboard = Controller()


# In[13]:


def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 


def curl():

    cap = cv2.VideoCapture(0)

    # Curl counter variables
    #window_name = 'DUMBBELL CURLS'
    counter = 0
    stage = None
    pincode = '----'
    num = "70"
    servo.write(num.encode())
    time.sleep(0.2)
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                #mp_drawing.DrawingSpec??

                # Calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)

                angle2 = calculate_angle(r_shoulder, r_elbow, r_wrist)

                # Visualize angle
                cv2.putText(image, str(angle), 
                               tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )

                cv2.putText(image, str(angle2),
                            tuple(np.multiply(r_elbow, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                # Curl counter logic
                if angle > 160:
                    if angle2 > 160:
                        stage = " down"
                if angle < 30:
                    if angle2 < 30 and stage == ' down':
                        stage=" up"
                        counter +=1
                        print(" " + counter)
                if counter==10:

                    pincode = '1530(s1)'

                if  counter==10 and stage ==' down':
                    num = '1'
                    servo.write(num.encode())
                    keyboard.press('q')
                    keyboard.release('q')

            except:
                pass

            # Render curl counter
            # Setup status box
            cv2.rectangle(image, (0,0), (500,73), (245,117,16), -1)

            # Rep data
            cv2.putText(image, 'REPS', (15,12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), 
                        (10,60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

            # Stage data
            cv2.putText(image, 'STAGE', (65,12), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, 
                        (80,60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
            
            cv2.rectangle(image, (500,0), (700,73), (0,0,0), -1)
            
            cv2.putText(image, 'PINCODE:', (500, 18),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 1, cv2.LINE_AA)
            
            cv2.putText(image, str(pincode), 
                        (500,50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            window_name = 'DUMBBELL CURLS'
           # cv2.rectangle(image, (0, 0), (500, 73), (245, 117, 16), -1)
            cv2.putText(image, str(window_name),
                        (200, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)



            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(window_name, image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                #time.sleep(10)
                num = "70"
                servo.write(num.encode())
                break
    cap.release()
    cv2.destroyAllWindows()



curl()
# In[14]:





# In[ ]:





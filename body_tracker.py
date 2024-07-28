import mediapipe as mp 
import cv2

# set up mediapipe tools
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# get webcam video
cap = cv2.VideoCapture(0)


with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        _, frame = cap.read()
        
        # color the feed
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        # detect
        results = holistic.process(img)

        # face landmarks
        mp_drawing.draw_landmarks(img,results.face_landmarks,mp_holistic.FACEMESH_TESSELATION)

        # show cam in a window
        cv2.imshow("camera input",img)

        if results.face_landmarks:
            mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
            # Extract the position of each face landmark
            for i, landmark in enumerate(results.face_landmarks.landmark):
                x = landmark.x 
                y = landmark.y 
                z = landmark.z 
                

        
        
        # press q to exit, & 0xFF is for compatibility across different OS
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        

cap.release()
cv2.destroyAllWindows()



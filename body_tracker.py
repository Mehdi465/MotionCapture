import mediapipe as mp 
import cv2

# set up mediapipe tools
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# get webcam video
cap = cv2.VideoCapture(0)


with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        # color the feed
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        # detect
        results = holistic.process(img)
        
        # draw result there are face_landmarks, pose_landmarks, right or left_hand_landmarks
        img = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    

        mp_drawing.draw_landmarks(img,results.face_landmarks,mp_holistic.FACEMESH_TESSELATION)
        # for pose
        mp_drawing.draw_landmarks(img,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
        frame_counter = 0
        # show cam in a window
        cv2.imshow("camera input",img)

        # press q to exit, & 0xFF is for compatibility across different OS
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()



import mediapipe as mp
import cv2

# Set up mediapipe tools
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Indices for left eye, right eye, and mouth landmarks (you can add more as needed)
LEFT_EYE_INDICES = [33, 133, 160, 159, 158, 157, 173, 154, 155, 145, 153, 144, 163, 7, 246]
RIGHT_EYE_INDICES = [362, 398, 384, 385, 386, 387, 388, 466, 388, 387, 386, 385, 384, 398, 362]
MOUTH_INDICES = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]

# Get webcam video
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Color the feed
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect
        results = holistic.process(img)
        
        # Convert back to BGR for drawing
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        if results.face_landmarks:
            # Extract and draw the position of left eye landmarks
            for i in LEFT_EYE_INDICES:
                landmark = results.face_landmarks.landmark[i]
                x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                y = int(landmark.y * frame.shape[0])
                cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
                
            # Extract and draw the position of right eye landmarks
            for i in RIGHT_EYE_INDICES:
                landmark = results.face_landmarks.landmark[i]
                x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                y = int(landmark.y * frame.shape[0])
                cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
                
            # Extract and draw the position of mouth landmarks
            for i in MOUTH_INDICES:
                landmark = results.face_landmarks.landmark[i]
                x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                y = int(landmark.y * frame.shape[0])
                cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        
        # Show cam in a window
        cv2.imshow("camera input", img)

        # Press q to exit, & 0xFF is for compatibility across different OS
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

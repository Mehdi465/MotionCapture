import mediapipe as mp 
import cv2
import threading

# Set up mediapipe tools
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Get webcam video
cap = cv2.VideoCapture(0)

# Global variable to store the result
results = None

def process_frame(holistic, img):
    global results
    results = holistic.process(img)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break

        # Color the feed
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Start a thread to process the frame
        thread = threading.Thread(target=process_frame, args=(holistic, img))
        thread.start()
        thread.join()

        # Draw results
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results:
            mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
            mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # Show cam in a window
        cv2.imshow("camera input", img)

        # Press q to exit, & 0xFF is for compatibility across different OS
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

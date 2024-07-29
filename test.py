import mediapipe as mp
import cv2

# Set up mediapipe tools
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Indices for various facial regions
LEFT_EYE_INDICES = [33, 133, 160, 159, 158, 157, 173, 154, 155, 145, 153, 144, 163, 7, 246]
RIGHT_EYE_INDICES = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
MOUTH_INDICES = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
LEFT_EYEBROW_INDICES = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]
RIGHT_EYEBROW_INDICES = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285]
FOREHEAD_INDICES = [9, 10, 338, 297, 332, 284, 251, 389, 356, 454, 323]
LEFT_CHEEK_INDICES = [187, 50, 101, 118, 117, 111, 120, 47, 115, 220, 237, 239, 241, 238, 20]
RIGHT_CHEEK_INDICES = [280, 350, 426, 429, 424, 356, 454, 374, 249]
LEFT_JAW_INDICES = [234, 93, 132, 58, 172, 136, 150, 176, 148, 152, 377, 378, 379, 365, 367]
RIGHT_JAW_INDICES = [454, 323, 366, 401, 368, 409, 270, 267, 397, 356, 452, 366, 401, 362]
NOSE = [1,2,3,4,5]
TEST_DOT = [188]

DEBUG = True
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
            # Function to draw specific landmarks
            def draw_landmarks(indices, color):
                for i in indices:
                    landmark = results.face_landmarks.landmark[i]
                    x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(img, (x, y), 2, color, -1)
            
            # Draw the position of specific landmarks

            if DEBUG:
                draw_landmarks(TEST_DOT, (0, 255, 0))

            else:         
                draw_landmarks(LEFT_EYE_INDICES, (0, 255, 0))
                draw_landmarks(RIGHT_EYE_INDICES, (0, 255, 0))
                draw_landmarks(MOUTH_INDICES, (0, 0, 255))
                draw_landmarks(LEFT_EYEBROW_INDICES, (255, 0, 0))
                draw_landmarks(RIGHT_EYEBROW_INDICES, (255, 0, 0))
                draw_landmarks(FOREHEAD_INDICES, (0, 255, 255))
                draw_landmarks(LEFT_CHEEK_INDICES, (255, 255, 0))
                draw_landmarks(RIGHT_CHEEK_INDICES, (255, 255, 0))
                draw_landmarks(LEFT_JAW_INDICES, (255, 0, 255))
                draw_landmarks(RIGHT_JAW_INDICES, (255, 0, 255))
                draw_landmarks(NOSE, (0, 255, 0))

        # Show cam in a window
        cv2.imshow("camera input", img)

        # Press q to exit, & 0xFF is for compatibility across different OS
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

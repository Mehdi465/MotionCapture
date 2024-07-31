import mediapipe as mp
import cv2

def draw_landmarks(indices, color):
                for i in indices:
                    landmark = results.face_landmarks.landmark[i]
                    x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(img, (x, y), 2, color, -1)
                    cv2.putText(img, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1, cv2.LINE_AA)

def get_test_points(steps:int)->list:
    list_res = []
    lines = []
    with open("list_point.txt","r") as list_file:
        lines = list_file.readlines()
    index = 0    
    for line in lines:
        if index>steps:
            break
        list_res.append(int(line.strip()))
        index +=1

    # rewrite the left points not yet processed
    with open("list_point.txt","+w") as list_file:
        list_file.writelines(lines[steps:])

    return list_res    

# Set up mediapipe tools
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Indices for various facial regions. Those indices are accurate
LEFT_EYE_INDICES = [33, 133, 160, 159, 158, 157, 173, 154, 155, 145, 153, 144, 163, 7, 246]
RIGHT_EYE_INDICES = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
MOUTH_INDICES = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
LEFT_EYEBROW_INDICES = [70, 63, 105, 66, 107, 55, 65, 52, 53, 46]
RIGHT_EYEBROW_INDICES = [336, 296, 334, 293, 300, 276, 283, 282, 295, 285]

# those indices are not accurate
FOREHEAD_INDICES = [9, 10, 338, 297, 332, 356, 454, 323,67,68,69,103,104,108,109,151,299,297,338,337]
LEFT_CHEEK_INDICES = [187, 50, 101, 118, 117, 111, 120, 47, 115, 220, 237, 239, 241, 238, 20, 50, 101,111,147]
RIGHT_CHEEK_INDICES = [280, 350, 426, 429, 424, 356, 454, 374, 249, 187 ,266,280, 340,345,349]
LEFT_JAW_INDICES = [234, 93, 132, 58, 172, 136, 150, 176, 148, 152, 377, 378, 379,34,58,93,132,138,135,136,149,150,172,215]
RIGHT_JAW_INDICES = [454, 323, 366, 401, 368, 409, 270, 267, 397, 356, 452, 401, 362, 288, 323, 329,364,361,367,411,435,451,454]
LEFT_TEMPE = [21,162]
LEFT_PAUPIERE = [27,28,29,30]
RIGHT_TEMPE = [251,301,356]
RIGHT_PAUPIERE = [260,258,257,259]
NOSE = [1,2,3,4,5,19,49,48,50,59,64,166,168,174,195,197,209,248,278,419,420,439]
CHIN = [32,140,152,148,200,211,262,368,318,395,18]           

DEBUG = False
# Get webcam video
cap = cv2.VideoCapture(0)

if DEBUG:
    TEST_DOT = get_test_points(20)

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
                draw_landmarks(CHIN, (255, 0, 0))
                draw_landmarks(LEFT_TEMPE,(255,255,255))
                draw_landmarks(RIGHT_TEMPE,(255,255,255))
        # Show cam in a window
        cv2.imshow("camera input", img)

        # Press q to exit, & 0xFF is for compatibility across different OS
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

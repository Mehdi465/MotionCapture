import mediapipe as mp
import cv2
import landmark_point as lp

def draw_landmarks(indices, color):
                for i in indices:
                    landmark = results.face_landmarks.landmark[i]
                    x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(img, (x, y), 2, color, -1)
                    cv2.putText(img, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1, cv2.LINE_AA)  

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


#### -------------- MAIN ------------- ##

if __name__ == "__main__":

    # Set up mediapipe tools
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
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
                    #draw_landmarks(lp.LEFT_EYE_INDICES, (0, 255, 0))
                    #draw_landmarks(RIGHT_EYE_INDICES, (0, 255, 0))
                    #draw_landmarks(MOUTH_INDICES, (0, 0, 255))
                    #draw_landmarks(LEFT_EYEBROW_INDICES, (255, 0, 0))
                    #draw_landmarks(RIGHT_EYEBROW_INDICES, (255, 0, 0))
                    #draw_landmarks(FOREHEAD_INDICES, (0, 255, 255))
                    #draw_landmarks(LEFT_CHEEK_INDICES, (255, 255, 0))
                    #draw_landmarks(RIGHT_CHEEK_INDICES, (255, 255, 0))
                    #draw_landmarks(LEFT_JAW_INDICES, (255, 0, 255))
                    #draw_landmarks(RIGHT_JAW_INDICES, (255, 0, 255))
                    #draw_landmarks(NOSE_INDICES, (0, 255, 0))
                    #draw_landmarks(CHIN_INDICES, (255, 0, 0))
                    #draw_landmarks(LEFT_TEMPE_INDICES,(255,255,255))
                    #draw_landmarks(RIGHT_TEMPE_INDICES,(255,255,255))
                    draw_landmarks(lp.RIGHT_EYEBROW_INDICES,(255,255,255))

            # Show cam in a window
            cv2.imshow("camera input", img)

            # Press q to exit, & 0xFF is for compatibility across different OS
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

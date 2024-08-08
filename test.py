import mediapipe as mp
import cv2
from landmark_point import LandmarkPoint as lp, Metaring

def draw_landmarks(indices, color):
                for i in indices:
                    landmark = results.face_landmarks.landmark[i]
                    x = int(landmark.x * frame.shape[1])  # Convert normalized coordinates to pixel values
                    y = int(landmark.y * frame.shape[0])
                    #z = landmark.z
                    cv2.circle(img, (x, y), 2, color, -1)
                    cv2.putText(img, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1, cv2.LINE_AA)


#### -------------- MAIN ------------- ##

if __name__ == "__main__":

    # Set up mediapipe tools
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    DEBUG = False

    # Get webcam video
    cap = cv2.VideoCapture(0)

    if DEBUG:
        TEST_DOT = None

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

                # extract position
                positions = Metaring.get_position(results,Metaring.DICT_METARING_LANDMARK_FACE)

                # draw all selected landmark
                draw_landmarks(list(Metaring.DICT_METARING_LANDMARK_FACE.values()),(255,255,255))

                print(positions)

            # Show cam in a window
            cv2.imshow("camera input", img)

            # Press q to exit, & 0xFF is for compatibility across different OS
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

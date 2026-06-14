

import cv2
import mediapipe as mp
import time

# Calculator function
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        emoji = ""
        result = None

        if op == '+':
            result = num1 + num2
            emoji = "😀"  # happy
        elif op == '-':
            result = num1 - num2
            emoji = "😢"  # sad
        elif op == '*':
            result = num1 * num2
            emoji = "😡"  # angry
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
                emoji = "🤣"  # funny
            else:
                print("Error: Division by zero")
                return None, ""
        else:
            print("Invalid operation")
            return None, ""

        print(f"Result: {result} {emoji}")
        return result, emoji

    except:
        print("Invalid input")
        return None, ""

# Mediapipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # warm up camera

smile_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    h, w, _ = frame.shape

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Mouth coordinates
            top_lip = face_landmarks.landmark[13]  # upper lip center
            bottom_lip = face_landmarks.landmark[14]  # lower lip center
            left_mouth = face_landmarks.landmark[78]  # left mouth corner
            right_mouth = face_landmarks.landmark[308]  # right mouth corner

            # Convert normalized coordinates to pixels
            top_lip_y = int(top_lip.y * h)
            bottom_lip_y = int(bottom_lip.y * h)
            left_x = int(left_mouth.x * w)
            right_x = int(right_mouth.x * w)

            # Calculate distances
            mouth_open = bottom_lip_y - top_lip_y
            mouth_width = right_x - left_x

            # Smile detection condition (adjust thresholds if needed)
            if mouth_width > 60 and mouth_open < 25:
                cv2.putText(frame, "Smile Detected!", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                smile_detected = True
                break

    cv2.imshow("Smile Detection", frame)

    if smile_detected:
        result, emoji = calculator()
        if result is not None:
            print("Closing webcam...")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

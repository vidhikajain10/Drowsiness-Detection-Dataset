import cv2
from utils import play_alarm

# Load cascades
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('models/haarcascade_eye.xml')

# Start webcam
cap = cv2.VideoCapture(0)

closed_frames = 0
threshold = 15  # increase if too sensitive

print("Starting system... Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Check eye state
        if len(eyes) == 0:
            closed_frames += 1
        else:
            closed_frames = 0

        # Draw face box
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Alert condition
        if closed_frames >= threshold:
            cv2.putText(frame, "DROWSINESS ALERT!", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
            play_alarm()

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

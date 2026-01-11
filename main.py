import cv2
from fer import FER

# initialize emotion detector
detector = FER()

# map prediction to emojis
emoji_map = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😡",
    "surprise": "😲",
    "disgust": "🤢",
    "fear": "😱",
    "neutral": "😐"
}

# start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # detect emotions
    emotions = detector.detect_emotions(frame)

    # copy frame for output
    display = frame.copy()

    for person in emotions:
        (x, y, w, h) = person["box"]
        emo, score = detector.top_emotion(frame)
        
        # draw face box
        cv2.rectangle(display, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # choose emoji
        emoji = emoji_map.get(emo, "🙂")
        
        # display text
        cv2.putText(display, f"{emo.upper()} {emoji}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Emoji Mood Predictor 🧠", display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

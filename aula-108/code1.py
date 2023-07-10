import cv2 
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence = 0.6, min_tracking_confidence = 0.5)
tipIds = [4,8,12,16,20]
def contarDedos(image, hand_landmarks, handNo = 0):
    
    fingers = []
    if hand_landmarks: 
        landmarks = hand_landmarks[handNo].landmark
        print("contar dedos")
        for i in tipIds: 
            finger_tip_y = landmarks[i].y
            finger_bottom_y = landmarks[i-2].y
            if i != 4:
                if finger_tip_y < finger_bottom_y:
                    fingers.append(1)
                else:
                    fingers.appends(0)
            total = fingers.count(1)
            texto = f"Dedos: {total}"
            cv2.putText(image, texto, (50, 50), cv2.FONT_HERSHEY_COMPLET, 1, (0, 0, 0), 2 )

def desenharMarcas(image, marcas):
    if marcas:
        for marca in marcas:
            mp_drawing.draw_landmarks(image, marca, mp_hands.HAND_CONNECTIONS)

while True:
    success, image = cap.read()
    if success:
        cv2.imshow("", image)

        results = hands.process(image)
        image = cv2.flip(image, 1)
        desenharMarcas(image, results.multi_hand_landmarks)
        contarDedos(image, results.multi_hand_landmarks)
    if cv2.waitKey(1) == 32:
        break

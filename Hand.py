import cv2
import numpy as np
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_drawing

class HandTracker:
    def __init__(self,pocet_ruka=2,detection=0.5,tracking=0.5):
        self.mp_hands = mp_hands
        self.mp_draw = mp_drawing
        # save library into the object

        hands_options = {
            "static_mode_image":False,
            "max_num_hands":pocet_ruka,
            "model_complexity":1,
            "min_detection_confidence": detection,
            "min_tracking_confidence": tracking
        }

        self.hands = self.mp_hands.Hands(**hands_options)
        self.result = None# no hand at first

    def find_hands(self, frame):
        rgb =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgb)

        hand_landmark = getattr(self.result,"multi_hand_landmarks",None)

        if hand_landmark:
            for landmarks in hand_landmark:
                connections = list(self.mp_hands.HAND_CONNECTIONS)

                self.mp_draw.draw_landmarks(frame,landmarks,connections)
        return frame

    def is_palm_open(self,hand_landmarks):
        lm = hand_landmarks.landmark


        fingers = [(8,6),(12,10),(16,14),(20,18)]

        extended = 0
        for tip,pip in fingers:
            if lm[tip].y < lm[pip].y:
                extended+=1

        return extended==4

    def get_palm_center(self,handlandmarks,frame_shape):
        h,w= frame_shape[:2]

        lm = handlandmarks.landmark

        point = [0,5,9,13,17]

        x = sum(lm[i].x for i in point)/len(point)
        y = sum(lm[i].y for i in point)/len(point)

        return int(x*w), int(y*h)


    def is_palm_up(self,handlandmarks,frame_shape):
        h,w = frame_shape[:2]

        lm = handlandmarks.landmark

        souradnice_wrist = np.array([
            lm[0].x *w,
            lm[0].y *h,
            lm[0].z *w
        ])

        souradnice_ukazovacek= np.array([
            lm[5].x *w,
            lm[5].y *h,
            lm[5].z *w
        ])


        souradnice_malicek = np.array([
            lm[17].x *w,
            lm[17].y *h,
            lm[17].z *w
        ])

        vector_na_dlane1 = souradnice_ukazovacek - souradnice_wrist
        vector_na_dlane2 = souradnice_malicek - souradnice_wrist

        normalova_vector = np.cross(vector_na_dlane1,vector_na_dlane2)

        delka_nv = np.linalg.norm(normalova_vector) # √x²*y²*z²

        if delka_nv < 1e-6:
            return False

        normalova_vector = normalova_vector - delka_nv

        return abs(normalova_vector[1])>0.65

    def is_hand_open(self,handlandmark):
        lm = handlandmark.landmark

        zapesti = np.array([
            lm[0].x,
            lm[0].y
        ])

        fingers = [
            (8, 6),    # Ngon tro
            (12, 10),  # Ngon giua
            (16, 14),  # Ngon ap ut
            (20, 18)   # Ngon ut
        ]

        extended = 0

        for tip_id,pip_id in fingers:
            tip = np.array([
                lm[tip_id].x,
                lm[pip_id].y
            ])

            pip = np.array([
                lm[pip_id].x,
                lm[pip_id].y
            ])

            tip_distance = np.linalg.norm(tip-zapesti)

            pip_distance = np.linalg.norm(pip - zapesti)

            if tip_distance > pip_distance *1.15:
                extended+=1

        return extended>=3

    def close(self):
        self.hands.close()

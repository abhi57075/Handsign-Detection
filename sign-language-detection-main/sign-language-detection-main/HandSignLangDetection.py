import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            finger_fold_status = []
            finger_fold_status2 = [] # used for vertical finger folds like to point upwards

            # print(lm_list) this contains co ordinates of all the dots
            # print(finger_fold_status) used for horizontal or along x axis for example in case of 'like'

            for tip in finger_tips:
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                # print(id, ":", x, y)

                cv2.circle(img, (x, y), 5, (25, 25, 25), cv2.FILLED)

                if lm_list[tip].x < lm_list[tip - 3].x:
                    cv2.circle(img, (x, y), 15, (0, 25, 0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)
                if lm_list[tip].y > lm_list[tip - 3].y:
                    cv2.circle(img, (x, y), 15, (0, 25, 0), cv2.FILLED)
                    finger_fold_status2.append(True)
                else:
                    finger_fold_status2.append(False)
            print(finger_fold_status)
            print(finger_fold_status2)

            if all(finger_fold_status):
                # Dislike
                if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y:
                    cv2.putText(img, "DISLIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)
                    print("DISLIKE")

                # like
                elif lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y:
                    print("LIKE")
                    cv2.putText(img, "LIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Left
            elif (lm_list[4].y < lm_list[2].y and lm_list[8].x < lm_list[6].x and lm_list[12].x > lm_list[10].x and lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x) :
                print("LEFT")
                cv2.putText(img, "LEFT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Right
            elif lm_list[4].y < lm_list[2].y and lm_list[8].x > lm_list[6].x and lm_list[12].x < lm_list[10].x and lm_list[16].x < lm_list[14].x and lm_list[20].x < lm_list[18].x:
                print("RIGHT")
                cv2.putText(img, "RIGHT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Rock and Roll
            elif lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and lm_list[16].y > lm_list[14].y and lm_list[20].y < lm_list[18].y:
                print("ROCK AND ROLL")
                cv2.putText(img, "ROCK AND ROLL", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Stop
            elif lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                print("STOP")
                cv2.putText(img, "STOP", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Up
            elif (lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[11].y and lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[4].x < lm_list[5].x) :
                    print("UP")
                    cv2.putText(img, "UP", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # L
            elif lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[11].y and lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                print("L")
                cv2.putText(img, "L", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Down
            elif (lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[4].x < lm_list[5].x) :
                    print("DOWN")
                    cv2.putText(img, "DOWN", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Call me
            elif (lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and lm_list[8].x < lm_list[6].x and lm_list[12].x < lm_list[10].x and lm_list[16].x < lm_list[14].x and lm_list[20].x > lm_list[18].x):
                print("CALL ME")
                cv2.putText(img, "CALL ME", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Peace
            elif (lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[8].x > lm_list[12].x and lm_list[4].x < lm_list[9].x and lm_list[4].x < lm_list[5].x) :
               print("PEACE")
               cv2.putText(img, "PEACE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            # Boom
            elif lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[4].y < lm_list[5].y :
               print("Boom")
               cv2.putText(img, "Boom", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)


            # superb
            elif lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                print("SUPERB")
                cv2.putText(img, "SUPERB", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            else:
                # HI
                if lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                    print("HI")
                    cv2.putText(img, "HI", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 0), 3)

            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 10, 255), 6, 3),
                                   mp_draw.DrawingSpec((0, 10, 255), 4, 2)
                                   )

    cv2.imshow("Hand Sign Detection", img)
    cv2.waitKey(1)

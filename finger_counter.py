import cv2
import mediapipe as mp


video = cv2.VideoCapture(2)


hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=3)
mpDraw = mp.solutions.drawing_utils

while True:
	check, img = video.read()
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = Hand.process(imgRGB)

	# Extraindo iformações
	hands_points = results.multi_hand_landmarks
	h, w, _ = img.shape

	if hands_points:
		for points in hands_points:
			print('----------- points', points)

			# draw the points
			mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
			for id, coord in enumerate(points.landmark):
				cx, cy = int(coord.x*w), int(coord.y*h)
				cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
	
	cv2.imshow("Imagem", img)
	cv2.waitKey(2)
    
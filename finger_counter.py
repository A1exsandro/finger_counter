import cv2
import mediapipe as mp


video = cv2.VideoCapture(2)


hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
	check, img = video.read()
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = Hand.process(imgRGB)

	# Extraindo iformações
	hands_points = results.multi_hand_landmarks
	h, w, _ = img.shape

	# dados para o contador
	arry_points = []

	if hands_points:
		for points in hands_points:

			# draw the points
			mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
			for id, coord in enumerate(points.landmark):
				cx, cy = int(coord.x*w), int(coord.y*h)
				cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

				# arry_points.append((id, cx, cy))
				arry_points.append((cx, cy))
				print('array points', arry_points)

			# Counter
			fingers = [8, 12, 16, 20]
			counter = 0
			if points:
				if arry_points[4][0] < arry_points[2][0]:
					counter +=1
				for finger in fingers:
					if arry_points[finger][1] < arry_points[finger-2][1]:
						counter +=1
			
			cv2.putText(img, str(counter), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,0), 5)
	
	cv2.imshow("Imagem", img)
	cv2.waitKey(2)
    
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
template = cv2.imread("pen.png", cv2.IMREAD_GRAYSCALE)
print(template.shape)
w, h = template.shape[::-1]



while True:
	_, frame = cap.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= 0.5)
	# frame2 = frame
	check = False
	for pt in zip(*loc[::-1]):
		x = cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
		print(x)
		print(pt)
		if (pt[0] > 600 and pt[1]> 100) and ( pt[0] + w < 700 and pt[1] + h < 500):
			# print(pt[0], pt[1])
			print('_______', pt)
			check = True
	if check:
		frame2 = cv2.rectangle(frame, (600,100), (700,500), (255,0,0), 3)
	else:
		frame2 = cv2.rectangle(frame, (600,100), (700,500), (255,255,0), 3)
	cv2.imshow("Frame", frame2)
	key = cv2.waitKey(1)
	if key == 27:
		break
cap.release()
cv2.destroyAllWindows()
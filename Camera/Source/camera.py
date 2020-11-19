from cv2 import *
from datetime import datetime
import numpy as np
import os

THRESHOLD = 80000
class VideoCamera:
	def __init__(self):
		self.camera = VideoCapture(0)
		_, self.last_frame = self.camera.read()
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		#if os.path.isfile("Camera/Data/"+ str(datetime.now().strftime("%d/%m/%y")) + ".avi") == False:
		self.now = datetime.now()
		self.writer = VideoWriter("Camera/Data/"+ str(self.now.strftime("%dT%mT%yT%HT%M")) + ".avi",  fourcc, 10.0,(int(self.camera.get(3)), int(self.camera.get(4) )))
		file = open("videos.txt", "a")
		file.write(self.now.strftime("%dT%mT%yT%HT%M,"))
		file.close()


	def get_frame(self):
		error, frame = self.camera.read()
		now = datetime.now()

		current_gray = cvtColor(frame, COLOR_BGR2GRAY)
		last_gray = cvtColor(self.last_frame, COLOR_BGR2GRAY)

		self.last_frame = frame
		net_difference = 0.0
		diff = subtract(current_gray, last_gray)
		width = np.size(diff, 0)
		height = np.size(diff, 1)

		for i in range(0, width, 5):
			for j in range(0, height, 5):
					r = diff[i, j]
					g = diff[i, j]
					b = diff[i, j]
					net_difference += (r+g+b)
		putText(frame, now.strftime("%d/%m/%y %H:%M:%S"), (int(self.camera.get(3) - 250), int(self.camera.get(3) - 250)), FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
		difference_frame = diff
		if net_difference > THRESHOLD:
			self.save_video(frame)
			putText(frame, "Moving", (20, 20), FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

		else:
			putText(frame, "Not Moving", (20, 20), FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
				

		
		ret, jpeg = cv2.imencode('.jpg', frame)
		_, difference = cv2.imencode('.jpg', difference_frame)
		return jpeg.tobytes(), difference.tobytes()

	def __del__(self):
		print("finishing the camera object")
		self.writer.release()
		
	def save_video(self, frame):
		self.writer.write(frame)

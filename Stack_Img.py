import cv2 
import os
import argparse
import time


ap = argparse.ArgumentParser(description='Input Stream to Image')
# ap.add_argument("-i", "--input", required=True,
# 	help="path to input video")
ap.add_argument("-o", "--output", required=True,
	help="path to output image")
ap.add_argument("-d", "--date", required=True,
	help="Required date")
ap.add_argument("-f", "--frame", required=True,
	help="Required frame count")
ap.add_argument("-c", "--camera", required=True,
        help="Required camera number one or two")
args = vars(ap.parse_args())

def getTime(start,end):
	hours, rem = divmod(end-start, 3600)
	minutes, seconds = divmod(rem, 60)
	currentTime = "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)
	return currentTime,int(hours)

p = os.path.join(args["output"], 'Img'+ args["date"])
if not os.path.exists(p):
	os.mkdir(p)
count = 0
cameratwo = 'rtsp://admin:123456@140.0.192.33:7070'
cameraone = 'rtsp://140.0.192.32/video1'
if args["camera"] == 'one':
	camera = cameraone
else:
	camera = cameratwo
image_count = 0
no_frame_count = 0
clear = lambda: os.system('clear')
hour = 0
start_time = time.time()
try:
	while True:
		vid = cv2.VideoCapture(camera)
		success, image = vid.read()
		end_time = time.time()
		if hour == 1:
			break
		while True:
			time_value, hour = getTime(start_time, end_time)
			name = args["date"] + 'img' + str(time_value) + '.jpg'
			if (count%int(args["frame"]) == 0) and success:
				cv2.imwrite(os.path.join(p, name), image) # save frame as JPEG file
				image_count += 1
			end_time = time.time()
			success,image = vid.read()
#	print('Read a new frame: ', success)
			if success == False:
				no_frame_count +=1
				if no_frame_count == 1000:
					break
			#if hour == 1:
				#break
			if success:
				count += 1
				no_frame_count = 0
		vid.release()
		clear()
except KeyboardInterrupt:
	pass

vid.release()
print('Total Number of valid image file read : ', count)
print('Total Number of image file saved : ', image_count)

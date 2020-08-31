import cv2 
import os
import argparse


ap = argparse.ArgumentParser(description='Input Stream to Video')
# ap.add_argument("-i", "--input", required=True,
#       help="path to input video")
ap.add_argument("-o", "--output", required=True,
        help="path to output Video")
ap.add_argument("-d", "--date", required=True,
        help="Required date")
ap.add_argument("-n", "--name", required=True,
        help="Required file Name")
args = vars(ap.parse_args())

#vidcap = cv2.VideoCapture('rtsp://admin:123456@140.0.192.33:7070')
vidcap = cv2.VideoCapture('rtsp://140.0.192.32/video1')
success,frame = vidcap.read()
frame_height, frame_width = frame.shape[:-1]
# print(frame_width, frame_height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
Name = args['name'] + '-' + args['date'] + '.avi'
output_file = cv2.VideoWriter(os.path.join(args['output'], Name),fourcc, 20.0, (frame_width,frame_height))

while True:
    success, frame = vidcap.read()
    if success:
        # write the flipped frame
        output_file.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
vidcap.release()
output_file.release()
cv2.destroyAllWindows()

# this file will get a lot of frames from my videos...
# this code is based on a course from my bachelor degree at UFRPE...

# to import you need to pip install opencv-python before...
import cv2

count = 0

def toFrame(path = ''):
    video = cv2.VideoCapture(path)
    (read, frame) = video.read()

    while(read):
        global count
        # remember: create the frames folder before run this!
        cv2.imwrite('frames/frame %d.jpg' % count, frame)

        count += 1
        read, frame = video.read()

toFrame('videos/video1.mp4')
toFrame('videos/video2.mp4')
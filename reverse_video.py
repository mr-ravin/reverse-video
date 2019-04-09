import numpy as np
import cv2 as cv

def video_file(input_file="input.avi",output_file="output.avi"):
 fourcc = cv.VideoWriter_fourcc(*'MJPG')
 out = cv.VideoWriter(output_file,fourcc, 20.0, (848,480))## output video file 
 cap = cv.VideoCapture(input_file) ## input video file
 frame_buffer=[]
 while cap.isOpened():
    ret, img = cap.read()
    frame_buffer.append(img)
 frame_buffer.reverse()
 for img in frame_buffer:
    out.write(img)
 cap.release()
 out.release()

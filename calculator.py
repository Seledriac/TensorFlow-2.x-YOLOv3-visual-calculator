import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import cv2
import numpy as np
import random
import time
import tensorflow as tf
from yolov3.yolov3 import Create_Yolov3
from yolov3.utils import detect_image
from yolov3.utils import detect_realtime
from yolov3.configs import *

input_size=YOLO_INPUT_SIZE

yolo = Create_Yolov3(input_size=input_size, CLASSES=TRAIN_CLASSES)
yolo.load_weights("./checkpoints/yolov3_calculator")

# use one :

# detect_image(yolo, image_path, "output_name", input_size=input_size, show=True, CLASSES=TRAIN_CLASSES, score_threshold=0.3, iou_threshold=0.45, rectangle_colors=(255,0,0), calculate=True)
# detect_realtime(yolo, "output_name", int_cap=1, input_size=input_size, show=True, CLASSES=TRAIN_CLASSES,  rectangle_colors=(255, 0, 0), calculate=True)
# detect_video(yolo, video_path, "output_name", input_size=input_size, show=False, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0), calculate=True)

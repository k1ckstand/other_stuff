#!/usr/bin/env python3

import os
import sys
import cv2
import numpy as np
from time import sleep

CHR_SET = ".:-=+*#%@"

def mapper(value: int, l_min: int, l_max: int, r_min: int, r_max: int) -> int:
    l_span = l_max - l_min
    r_span = r_max - r_min
    s_value = (value - l_min) / l_span
    return int(r_min + (s_value * r_span))

def video() -> None:
    '''Display video in the terminal'''
    try:
        vid = cv2.VideoCapture(0)
        while True:
            _, frame = vid.read()  
            os.system('clear')
            print_image(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                vid.close()
                break
            sleep(.1)
        vid.close()
    except Exception as e:
        print("Something went wrong with video")
        print(e)

def print_image(frame: np.array) -> None:
    try:
        frame = cv2.resize(frame, None, fx=.1, fy=.1) 
        for y in frame:
            for x in y:
                color_avg = x.sum() // 3
                print(CHR_SET[mapper(color_avg, 0, 256, 0, len(CHR_SET))], end='')
            print('')
    except Exception as e:
        print("Something went wrong with print_image.")
        print(e)

def image(img):
    print_image(cv2.imread(img))
    print(type(cv2.imread(img)))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for img in sys.argv:
            image(img)
    else: video()

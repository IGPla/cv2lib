
# -*- coding: utf-8 -*-
"""
Capture utils functions
"""
import cv2


class CaptureWrapper(object):
    """
    Capture wrapper
    """

    def __init__(self, cam_num=0):
        self.cam_num = cam_num
        self.capture = cv2.VideoCapture(self.cam_num)
        if not self.capture.isOpened():
            raise Exception("Cannot open camera")

    def get_frame(self):
        return self.capture.read()

    def close(self):
        return self.capture.release()

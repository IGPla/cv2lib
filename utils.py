# -*- coding: utf-8 -*-
"""
General purpose functions
"""
import cv2


def get_keycode(wait_time=1):
    """
    Return keycode rectified if exists
    """
    keycode = cv2.waitKey(wait_time)
    if keycode != -1:
        keycode &= 0xFF
    return keycode

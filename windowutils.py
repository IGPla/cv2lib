# -*- coding: utf-8 -*-
"""
Window util functions
"""
import cv2

WINDOW_NAME = "default"


# WINDOW
def create_window(window_name=WINDOW_NAME):
    """
    Create a window
    """
    cv2.namedWindow(window_name)


def destroy_window(window_name=WINDOW_NAME):
    """
    Destroy a window
    """
    cv2.destroyWindow(window_name)


def show_image(image, window_name=WINDOW_NAME):
    """
    Show image
    """
    cv2.imshow(window_name, image)

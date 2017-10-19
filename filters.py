# -*- coding: utf-8 -*-
"""
Filter functions here
"""
import cv2
import numpy as np


class BaseImageFilter(object):
    """
    Base filter, scaffolding common filter usage
    """

    def __init__(self, kernel):
        self._kernel = kernel

    def filter(self, src, dst):
        cv2.filter2D(src, -1, self._kernel, dst)


class SharpFilter(BaseImageFilter):
    """
    Sharp filter
    """

    def __init__(self):
        kernel = np.array([
            [-2, -2, -2],
            [-2, 18, -2],
            [-2, -2, -2]
        ])
        super(SharpFilter, self).__init__(kernel)


class EdgeHighlightFilter(BaseImageFilter):
    """
    Highlight edges
    """

    def __init__(self):
        kernel = np.array([
            [-2, -2, -2],
            [-2, 17, -2],
            [-2, -2, -2]
        ])
        super(EdgeHighlightFilter, self).__init__(kernel)


class BlurFilter(BaseImageFilter):
    """
    Basic blur
    """

    def __init__(self):
        kernel = np.array([
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04]
        ])
        super(BlurFilter, self).__init__(kernel)

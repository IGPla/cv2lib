# -*- coding: utf-8 -*-
"""
Video writer utils
"""
import cv2


class WriterWrapper(object):
    """
    Writter wrapper
    """

    def __init__(self, destiny_file,
                 fourcc=cv2.VideoWriter_fourcc("M", "J", "P", "G"),
                 fps=24.0,
                 size=(640, 480),
                 capture=None):
        """
        If capture is passed, fps and size will be retrieved from it
        """
        if capture:
            fps = capture.get(cv2.CAP_PROP_FPS)
            size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        self.writer = cv2.VideoWriter(destiny_file,
                                      fourcc,
                                      fps,
                                      size)

    def write(self, frame):
        self.writer.write(frame)

    def close(self):
        self.writer.release()

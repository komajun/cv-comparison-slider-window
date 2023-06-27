import copy
import numpy as np
import cv2 as cv

from cv_comparison_slider_window import CvComparisonSliderWindow


def main():
    cvwindow = CvComparisonSliderWindow(
        window_name='debug',
        line_color=(255, 255, 255),
        line_thickness=1,
    )

    cap1 = cv.VideoCapture("source-saliency-aware_sample_1m_1.mkv")
    cap2 = cv.VideoCapture("sample_1m_1.mkv")
    frame_count = int(cap1.get(cv.CAP_PROP_FRAME_COUNT))

    for i in range(frame_count):
        ret, frame1 = cap1.read()
        ret, frame2 = cap2.read()
        if not ret:
            continue

        cvwindow.imshow(frame1, frame2)

        key = cv.waitKey(33)
        if key == 27:  # ESC
            break

    cap1.release()
    cap2.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
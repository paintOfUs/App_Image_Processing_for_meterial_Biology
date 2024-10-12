import cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal

class ImageProcessingThread(QThread):
    processing_finished = pyqtSignal(object, object, object, object, list)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        img = cv2.imread(self.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = img[:, :, 0]

        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 70, 150, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        erode = cv2.erode(thresh, kernel, iterations=1)
        contours, _ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        count = 0
        info = []
        contour_image = img.copy()
        for i, contour in enumerate(contours):
            (x, y), radius = cv2.minEnclosingCircle(contour)
            diameter = radius * 2
            if diameter > 1.0:
                count += 1
                center = (int(x), int(y))
                text = f'{i + 1}'
                cv2.putText(contour_image, text, center, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
                cv2.drawContours(contour_image, [contour], -1, (0, 255, 0), 2)
                cv2.circle(contour_image, (int(x), int(y)), int(radius), (0, 0, 255), 4)
                mask = np.zeros_like(gray, dtype=np.uint8)
                cv2.circle(mask, center, int(radius), 255, thickness=-1)
                circle_pixel_coords = [(x, y) for y in range(mask.shape[0]) for x in range(mask.shape[1]) if mask[y, x] == 255]
                circle_pixel_values = [gray[y, x] for x, y in circle_pixel_coords]
                item = [i, x, y, radius, diameter, circle_pixel_values]
                info.append(item)
        
        self.processing_finished.emit(img, gray, erode, contour_image, info)

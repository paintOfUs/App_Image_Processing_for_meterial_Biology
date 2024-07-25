import cv2
import numpy as np
class img_process():
    def read_img(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
    
    def img2gray(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img
    
    def processing(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = cv2.resize(img,(480,640))
        gray = img[:,:,0]
        
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, thresh = cv2.threshold(blur, 70, 150, cv2.THRESH_BINARY)
        # Tạo kernel (structuring element) - kích thước 3x3
        kernel = np.ones((3, 3), np.uint8)

        # Thực hiện erode
        erode = cv2.erode(thresh, kernel, iterations=1)
        
        # Tìm kiếm contour
        contours, _ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        count = 0
        # Tạo một danh sách để lưu các histogram của mỗi contour
        histograms = []
        info = []
        # Vẽ contour và vòng tròn bao quanh lên ảnh gốc
        contour_image = img.copy()
        # Tính toán và in đường kính của từng contour
        for i, contour in enumerate(contours):
            # Tìm vòng tròn bao quanh nhỏ nhất
            (x, y), radius = cv2.minEnclosingCircle(contour)
            diameter = radius * 2
            if diameter > 1.0:
                count+=1
                print(f"Contour {i + 1}:")
                print(f"  - tâm: ({x:.2f}, {y:.2f})")
                print(f"  - Bán kính: {radius:.2f}")
                print(f"  - Đường kính: {diameter:.2f}")
                
                # Chuyển đổi tọa độ gốc của text thành số nguyên
                center = (int(x), int(y))
                # Gắn text lên ảnh tại điểm trung tâm
                text = f'{i + 1}'
                cv2.putText(contour_image, text, center, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
                cv2.drawContours(contour_image, [contour], -1, (0, 255, 0), 2)  # Vẽ contour bằng màu xanh lá cây
                cv2.circle(contour_image, (int(x), int(y)), int(radius), (0, 0, 255), 4)  # Vẽ vòng tròn bằng màu đỏ
                
                # Tính toán cường độ sáng
                # Tạo một mask (mặt nạ) với kích thước giống ảnh gốc
                mask = np.zeros_like(gray, dtype=np.uint8)

                # Vẽ vòng tròn lên mask
                cv2.circle(mask, center, int(radius), 255, thickness=-1)
                
                # Tạo một danh sách để lưu tọa độ của các pixel nằm trong vòng tròn
                circle_pixel_coords = []

                # Lấy tọa độ của các pixel nằm trong vòng tròn
                for y in range(mask.shape[0]):
                    for x in range(mask.shape[1]):
                        if mask[y, x] == 255:
                            circle_pixel_coords.append((x, y))

                # Tính toán cường độ sáng của các pixel nằm trong vòng tròn
                # Tính toán cường độ sáng trung bình
                circle_pixel_values = [gray[y, x] for x, y in circle_pixel_coords]
                item = [i,x,y,radius,diameter,circle_pixel_values]
                info.append(item)
        
        return img, gray, erode, contour_image, info

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
from UI import *
from image_processing import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.process = img_process()
        self.ui.setupUi(self)
        self.ui.btn_img.clicked.connect(self.btnImg)
        
    #Chuyển ảnh sang dạng bitmap và thêm vào qlabel đúng tỉ lệ
    def numpy2pixmap(self, img, qlabel):
        if len(img.shape) == 2:  # Grayscale image
            h, w = img.shape
            image = QImage(img.data.tobytes(), w, h, w, QImage.Format.Format_Grayscale8)
        if len(img.shape) == 3:
            h,w,ch = img.shape
            image = QImage(img.data, w, h, ch * w, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(qlabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        qlabel.setPixmap(pixmap)
        qlabel.setScaledContents(True)
    
    def setTable(self,info, table):
        table.tableWidget.setRowCount(len(info))
        for i, data in enumerate(info):
            for j, value in enumerate(data):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                table.tableWidget.setItem(i, j, item)
        
    
    #Sự kiện Click
    def btnImg(self):
        path,_ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "All Files (*);; Python Files (*.py);; PNG Files (*.png)",
        )
        img, gray, thresh, countour_img, info = self.process.processing(path)
        self.numpy2pixmap(img,self.ui.img1)
        self.numpy2pixmap(gray,self.ui.img2)
        self.numpy2pixmap(thresh,self.ui.img3)
        self.numpy2pixmap(countour_img,self.ui.img4)
        self.setTable(info, self.ui)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
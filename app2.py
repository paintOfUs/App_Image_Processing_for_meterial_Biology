
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1284, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1281, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.menu = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.menu.setObjectName("menu")
        self.btn_img = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_img.setObjectName("btn_img")
        self.menu.addWidget(self.btn_img)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.menu.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.menu.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.menu.addWidget(self.pushButton_4)
        self.low_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.low_label.setGeometry(QtCore.QRect(900, 40, 81, 31))
        self.low_label.setObjectName("low_label")
        self.low = QtWidgets.QSlider(parent=self.centralwidget)
        self.low.setGeometry(QtCore.QRect(900, 71, 251, 31))
        self.low.setMaximum(255)
        self.low.setPageStep(10)
        self.low.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.low.setObjectName("low")
        self.hight_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hight_label.setGeometry(QtCore.QRect(900, 120, 71, 21))
        self.hight_label.setObjectName("hight_label")
        self.hight = QtWidgets.QSlider(parent=self.centralwidget)
        self.hight.setGeometry(QtCore.QRect(900, 160, 251, 31))
        self.hight.setMaximum(255)
        self.hight.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.hight.setObjectName("hight")
        self.low_display = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.low_display.setGeometry(QtCore.QRect(1160, 70, 71, 31))
        self.low_display.setObjectName("low_display")
        self.high_display = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.high_display.setGeometry(QtCore.QRect(1160, 160, 71, 31))
        self.high_display.setObjectName("high_display")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(880, 210, 401, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 861, 631))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.img2 = QtWidgets.QLabel(parent=self.widget)
        self.img2.setStyleSheet("background-color: rgb(85, 170, 255)")
        self.img2.setObjectName("img2")
        self.gridLayout.addWidget(self.img2, 0, 1, 1, 1)
        self.img3 = QtWidgets.QLabel(parent=self.widget)
        self.img3.setStyleSheet("background-color: rgb(85, 170, 255)")
        self.img3.setObjectName("img3")
        self.gridLayout.addWidget(self.img3, 1, 0, 1, 1)
        self.img4 = QtWidgets.QLabel(parent=self.widget)
        self.img4.setStyleSheet("background-color: rgb(85, 170, 255)")
        self.img4.setObjectName("img4")
        self.gridLayout.addWidget(self.img4, 1, 1, 1, 1)
        self.img1 = QtWidgets.QLabel(parent=self.widget)
        self.img1.setStyleSheet("background-color: rgb(85, 170, 255)")
        self.img1.setObjectName("img1")
        self.gridLayout.addWidget(self.img1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_img.setText(_translate("MainWindow", "Đọc ảnh"))
        self.pushButton.setText(_translate("MainWindow", "Áp dụng ngưỡng"))
        self.pushButton_3.setText(_translate("MainWindow", "Xử lý ảnh"))
        self.pushButton_4.setText(_translate("MainWindow", "Chức năng khác"))
        self.low_label.setText(_translate("MainWindow", "Ngưỡng dưới"))
        self.hight_label.setText(_translate("MainWindow", "Ngưỡng trên"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Contour"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tâm"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bán Kính"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Đường kính"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cường độ sáng"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Image"))
        self.img2.setText(_translate("MainWindow", "TextLabel"))
        self.img3.setText(_translate("MainWindow", "TextLabel"))
        self.img4.setText(_translate("MainWindow", "TextLabel"))
        self.img1.setText(_translate("MainWindow", "TextLabel"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = None  # Để lưu trữ hình ảnh
        self.btn_img.clicked.connect(self.load_image)
        self.pushButton.clicked.connect(self.apply_threshold)
        self.pushButton_3.clicked.connect(self.process_image)
        self.pushButton_4.clicked.connect(self.another_function)
        self.low.valueChanged.connect(self.updateThreshold)
        self.hight.valueChanged.connect(self.updateThreshold)
    
    def load_image(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setNameFilter("Image files (*.png *.jpg *.bmp)")
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.image = cv2.imread(file_path)
            self.show_image(self.image, self.img1)  # Hiển thị ảnh ở QLabel img1
            self.updateThreshold()
    
    def show_image(self, img, label):
        if img is None:
            return
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        q_img = QImage(rgb_image.data, w, h, ch * w, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        label.setPixmap(pixmap)
    
    def apply_threshold(self):
        if self.image is None:
            return
        low = self.low.value()
        high = self.hight.value()
        _, thresh_img = cv2.threshold(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), low, high, cv2.THRESH_BINARY)
        self.show_image(thresh_img, self.img2)  # Hiển thị ảnh ngưỡng ở QLabel img2
    
    def process_image(self):
        if self.image is None:
            return
        low = self.low.value()
        high = self.hight.value()
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh_img = cv2.threshold(gray, low, high, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.show_image(thresh_img, self.img2)  # Hiển thị ảnh ngưỡng ở QLabel img2
        self.update_table(contours)
    
    def another_function(self):
        # Implement another function
        pass

    def update_table(self, contours):
        self.tableWidget.setRowCount(0)  # Xóa tất cả các hàng cũ
        for i, contour in enumerate(contours):
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            radius = int(np.sqrt(M["m00"] / np.pi))
            diameter = 2 * radius
            intensity = np.mean(self.image[contour[:, :, 1], contour[:, :, 0]])
            
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(i)))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(f"({cX}, {cY})"))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(radius)))
            self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(diameter)))
            self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(intensity)))
            self.tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(f"Image {i+1}"))

    def updateThreshold(self):
        low = self.low.value()
        high = self.hight.value()
        self.low_display.setText(str(low))
        self.high_display.setText(str(high))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

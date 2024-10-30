import cv2
import requests
from PySide6.QtCore import QSize, QRect, QUrl, QUrlQuery, QJsonDocument, QByteArray
from PySide6.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QImage, QPixmap, QImageReader
import sys
from shiyan import Ui_shiyan
from pathlib import Path
import base64

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_shiyan()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        #发送一个信号，并将信号插入对应的槽函数中
        # self.ui.imageButton.clicked.connect(self.show_img_with_ImageReader_Scaled("trt4.tiff", self.ui.showLabel, scaledSize))
        # self.ui.imageButton.clicked.connect(self.show_img_with_ImageReader_Clip(r"D:\Qtwork\Test3\trt4.tiff", self.ui.showLabel, clipRect))
        self.ui.imageButton.clicked.connect(self.showImage)
        # self.ui.imageButton.clicked.connect(self.show_img_with_ImageReader(r"D:\Qtwork\Test3\try.jpg", self.ui.showLabel))
    def showImage(self):
        #修改成自己的路径
        path = r"D:\HUST\code\imagingSystem\imagingSystem\application\ui\test\test.jpg"
        area_x = 0
        area_y = 0
        width = 0
        height = 0
        response = requests.get("http://127.0.0.1:8000/api/imageShow/", params={"path": path, "area_x": area_x, "area_y": area_y, "width": width, "height": height})
        if response.status_code == 200:
            print("获取成功！")
            data = response.json()
            image_bytes = base64.b64decode(data)
            image = QImage()
            image.loadFromData(image_bytes)
            self.ui.showLabel.setPixmap(QPixmap.fromImage(image))
            self.ui.showLabel.setScaledContents(True)
        else:
            print("获取失败！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())

import os
import sys
import time

import PIL
from PIL import Image

from PyQt5 import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox, QProgressBar
from PyQt5.QtCore import Qt


class MainFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Resizer")
        self.setWindowIcon(QIcon("windowIcon.jpg"))
        self.setFixedWidth(600)
        self.setFixedHeight(400)
        #self.resize(500, 400)
        self.setStyleSheet("background-color: floralwhite;")

        self.myFont = QFont()
        self.myFont.setBold(True)

        self.lbl_path = QLabel(self)
        self.lbl_path.setGeometry(50, 20, 100, 30)
        self.lbl_path.setText("Folder\'s Path : ")
        self.lbl_path.setStyleSheet("font-size: 12px; ")
        self.lbl_path.setFont(self.myFont)
        self.lbl_path.show()

        self.tf_path = QLineEdit(self)
        self.tf_path.setGeometry(200, 20, 200, 30)
        self.tf_path.setStyleSheet("border: 2px solid black");
        self.tf_path.show()

        self.lbl_width = QLabel(self)
        self.lbl_width.setGeometry(50, 100, 150, 30)
        self.lbl_width.setText("Enter Desired Width : ")
        self.lbl_width.setStyleSheet("font-size: 12px; ")
        self.lbl_width.setFont(self.myFont)
        self.lbl_width.show()

        self.tf_width = QLineEdit(self)
        self.tf_width.setGeometry(200, 100, 200, 30)
        self.tf_width.setStyleSheet("border: 2px solid black");
        self.tf_width.show()

        self.lbl_height = QLabel(self)
        self.lbl_height.setGeometry(50, 150, 150, 30)
        self.lbl_height.setText("Enter Desired Height : ")
        self.lbl_height.setStyleSheet("font-size: 12px; ")
        self.lbl_height.setFont(self.myFont)
        self.lbl_height.show()

        self.tf_height = QLineEdit(self)
        self.tf_height.setGeometry(200, 150, 200, 30)
        self.tf_height.setStyleSheet("border: 2px solid black")
        self.tf_height.show()

        self.aspectRatio = QCheckBox(self)
        self.aspectRatio.setText("Maintain Aspect Ratio")
        self.aspectRatio.setGeometry(200, 190, 200, 50)
        self.aspectRatio.show()

        self.pbtn_resize = QPushButton(self)
        self.pbtn_resize.setText('Resize')
        self.pbtn_resize.setGeometry(300, 270, 200, 50)
        self.pbtn_resize.setFont(self.myFont)
        self.pbtn_resize.setStyleSheet("background-color: mintcream; color: black; font-size: 12px; border: 2px solid black")
        self.pbtn_resize.show()
        self.pbtn_resize.clicked.connect(lambda: func_imageResize(self.tf_path, self.tf_width, self.tf_height))


        def func_imageResize(path, width, height):

            if self.aspectRatio.isChecked() == True:
                newHeight = 0
            else:
                newHeight = height.text()
                newHeight = int(newHeight)

            imageLocation = path.text()
            fixedWidth = width.text()
            fixedWidth = int(fixedWidth)

            for image_file in os.listdir(imageLocation):
                if image_file.endswith(".jpg") or image_file.endswith(".JPG") or image_file.endswith(".png"):
                    image = Image.open(imageLocation + '\\' + image_file)
                    if newHeight == 0:
                        newHeight = int((image.size[1] / image.size[0]) * (fixedWidth))
                    resized_image = image.resize((fixedWidth, newHeight), PIL.Image.NEAREST)
                    resized_image.save(imageLocation + '\\' + image_file)


            msgBox = QMessageBox(self)
            msgBox.setWindowTitle("Message")
            msgBox.setText("Images have been resized successfully.")
            msgBox.exec()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    cls_mainFrame = MainFrame()

    cls_mainFrame.show()

    sys.exit(app.exec_())






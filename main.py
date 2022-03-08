Byunghwan Jeon, Hankuk University of Foreign Studies
Touched by user2
second Touched by user2


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import numpy as np
import qimage2ndarray #pip install qimage2ndarray


form_class = uic.loadUiType('D:\\project\\opensw\\image.ui')[0] #경로지정

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.npCanvas = np.ones((300,500,1), dtype='uint8') 

    def drawImage(self):
        #qPixmapVar = QPixmap()
        #qPixmapVar.load("image.png")

       # self.npCanvas = np.ones((300,500,1), dtype='uint8')     #y, x, c
       # self.npCanvas *= 200                                                                                                                                                                              
        #im_np = np.transpose(im_np, (1,0,2))                                                                                                                                                                              
        #qimage = QImage(im_np, im_np.shape[0], im_np.shape[1], QImage.Format_Mono)    #Format_RGB888

        #self.npCanvas *= 200
        qimage = qimage2ndarray.array2qimage(self.npCanvas, normalize=False)
        #qimage = qwt.toqimage.array_to_qimage(im_np, copy=False)

        pixmap = QPixmap(qimage)
        #pixmap_label.setPixmap(pixmap)

        self.label1.setPixmap(pixmap)
        print(self.label1.geometry())

    def drawDot(self, x, y, val):
        self.npCanvas[y, x] = val
        
                


                   


app = QApplication(sys.argv)
mainWindow = WindowClass()

for i in range(10):
    mainWindow.drawDot(50, 50+i, 255)

mainWindow.drawImage()


mainWindow.show()
app.exec()

import sys
import os
from PyQt5.QtWidgets import QMainWindow,QApplication, qApp, QFileDialog
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import glob


form_class = loadUiType("imageViewer.ui")[0]

class Node:
    def __init__(self, item=None, link = None):
        self.item = item
        self.link = link
        
class CircleLinkedList:
    def __init__(self):
        self.root = Node()
        self.tail = self.root
        self.current = self.root
        
    def append(self, item):
        newNode = Node(item)
        if self.root.item == None:
            self.root = newNode
            self.tail = newNode
            newNode.link = self.root
        else:
            self.tail.link = newNode
            newNode.link = self.root
            self.tail = newNode

    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != self.root:
            curNode = curNode.link
            print(curNode.item)

    def listSize(self):
        curNode = self.root
        cnt = 1
        while curNode.link != self.root:
            curNode = curNode.link
            cnt += 1
        return cnt

    def setCurrent(self,item):
        curNode = self.root
        for i in range(self.listSize()):
            if curNode.item != item:
                curNode = curNode.link
            else:
                self.current = curNode
                break
    
    def moveNext(self):
        self.current = self.current.link
        print("현재 위치는 ", self.current.item, "입니다.")

    def insert(self, item):
        newNode = Node(item)
        _tmp = self.current.link
        self.current.link = newNode
        newNode.link = _tmp
        if self.current == self.tail:
            self.tail = newNode

    def delete(self, item):
        delYN = False
        curNode = self.root
        if curNode.item == item:
            self.root = self.root.link
            self.tail.link = self.root
            delYN = True
        else:
            while curNode.link != self.root:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                    if curNode == self.tail:
                        self.tail = preNode
                    delYN = True
        if delYN == False: 
            print("delete failed")

class ViewerClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.qPixmapVar = QPixmap()
        self.actionSelect.triggered.connect(self.fileSelect)
        self.pushButton.clicked.connect(self.moveNextClick)
        self.slideShowButton.clicked.connect(self.slideShowClick)
        # self.shuffleButton.clicked.connect(self.shuffleClick)
        self.actionExit.triggered.connect(qApp.quit)

    def fileSelect(self):
        dirName = QFileDialog.getExistingDirectory(self,"Open Folder")
        self.files = CircleLinkedList()
        for file in glob.glob(os.path.join(dirName,'*.jpg')):
            self.files.append(file)
        self.files.current = self.files.root
        self.qPixmapVar = self.qPixmapVar.scaled(700, 400, aspectRatioMode=True)
        self.label.setPixmap(self.qPixmapVar)

    def moveNextClick(self):
        self.files.moveNext()
        self.qPixmapVar.load(self.files.current.item)
        self.qPixmapVar = self.qPixmapVar.scaled(700,400,aspectRatioMode=True)
        self.label.setPixmap(self.qPixmapVar)
    def slideShowClick(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.moveNextClick)
        self.timer.start(3000)
        
app = QApplication(sys.argv)
myWindow = ViewerClass(None)
myWindow.show()
app.exec_()
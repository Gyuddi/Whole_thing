import sys

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUiType

form_class=loadUiType("SimpleCalc.ui")[0]

class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def isEmpty(self):
        return len(self.s) == 0 # True, False

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def size(self):
        return len(self.s)

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

class CalcClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        nums = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        for number in nums:
            number.clicked.connect(self.Nums)

        self.bDel.clicked.connect(self.bDelClick)
        self.bClear.clicked.connect(self.bClearClick)
        self.bRun.clicked.connect(self.bRunClick)
        self.bPlus.clicked.connect(self.bPlusClick)
        self.bMinus.clicked.connect(self.bMinusClick)
        self.bMult.clicked.connect(self.bMultClick)
        self.bDivide.clicked.connect(self.bDevideClick)
        self.bDot.clicked.connect(self.bDotClick)

    def isOper(self,item):
        if item == '+' or item == '-' or item == '*' or item == '/':
            return True
        else:
            return False


    def isNum(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def Postfix(self,eq):
        eqList = list(eq)
        s = Stack()
        postEq = []

        for item in eqList:
            if item == '(':
                s.push(item)
            elif item == ')':
                while True:
                    _tmp = s.pop()
                    if _tmp == '(':
                        break
                    else:
                        postEq.append(_tmp)
            elif item == "+" or item == "-":
                while self.isOper(s.peek()) == True:
                    postEq.append(s.pop())
                s.push(item)
            elif item == "*" or item == "/":    
                while s.peek() == "*" or s.peek() == "/":
                    postEq.append(s.pop())
                s.push(item)
            elif self.isNum(item) == True:
                postEq.append(item)
        while s.isEmpty() == False:
            postEq.append(s.pop())
        print(postEq)

        S = Stack()
        for item in postEq:
            if self.isOper(item) == False:
                S.push(item)
            else:
                num2 = float(S.pop())
                num1 = float(S.pop())
                if item == '+': S.push(str(num1 + num2))
                elif item == '-': S.push(str(num1 - num2))   
                elif item == '*': S.push(str(num1 * num2)) 
                elif item == '/': S.push(str(num1 / num2))
        return(S.pop())


    def Nums(self):
        sender = self.sender()
        numTxt = sender.text()
        if self.result.text() == "0":
            self.result.setText(numTxt)
        else:
            self.result.setText(self.result.text()+numTxt)

    def bDotClick(self):
        self.result.setText(self.result.text()+".")
    def bPlusClick(self):
        self.result.setText(self.result.text()+"+")
    def bMinusClick(self):
        self.result.setText(self.result.text()+"-")
    def bDevideClick(self):
        self.result.setText(self.result.text()+"/")
    def bMultClick(self):
        self.result.setText(self.result.text()+"*")

    def bDelClick(self):
        n=len(self.result.text())
        self.result.setText(self.result.text()[0:n-1])

    def bClearClick(self):
        self.result.setText("0")


    def bRunClick(self):
        eq = self.result.text()
        print(eq)
        result = self.Postfix(self.result.text())
        print(result)
        self.result.setText(str(result))

app=QApplication(sys.argv)
myWindow=CalcClass(None)
myWindow.show()
app.exec_()

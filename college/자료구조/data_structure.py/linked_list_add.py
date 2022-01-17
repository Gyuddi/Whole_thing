class Node:
    def __init__(self, item = None, link = None): 
        self.item = item
        self.link = link

class LinkedList:
    def __init__(self):
        self.root = Node()

    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if curNode.item == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
    
    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != None:
            curNode = curNode.link
            print(curNode.item)
    
    def listSize(self):
        if self.root == None:
            return 0
        curNode = self.root
        cnt = 1
        while curNode.link != None:
            curNode = curNode.link
            cnt += 1
        return cnt
            
    def insert(self, idx, item):
        n = self.listSize()
        if idx < 0 or idx >= n:
            print("index range error")
        else:
            newNode = Node(item)
            curNode = self.root
            if idx == 0:
                _tmp = self.root
                self.root = newNode
                newNode.link = _tmp
            else:
                for curIdx in range(idx-1):
                    curNode = curNode.link
                _tmp = curNode.link
                curNode.link = newNode
                newNode.link = _tmp
    
    def find(self, item):
        find = -1
        idx = 0
        if self.root.item == item:
            find += 1
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link
                idx += 1
                if curNode.item == item:
                    find = idx
                    break
        return find
    
    def delete(self,item):
        delYN = False
        curNode = self.root
        preNode = curNode
        if curNode.item == item:
            self.root = self.root.link
            delYN = True
        else:
            while curNode.link != None:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                    delYN = True
        if curNode.item == item:
            preNode.link = None
            delYN = True
        if delYN == False:
            print("delete failed")

    def peek(self):
        return self.root.item[1]

    def pop(self):
        _tmp = self.root 
        self.root = _tmp.link
        return _tmp.item
        
    def get(self, idx):
        curNode = self.root
        for i in range(idx):
            curNode = curNode.link
        return curNode.item


class Poly:
    def __init__(self):
        self.parm = LinkedList()

    def setParm(self, coef, order):
        self.parm.append([coef, order])

    def peek(self):
        return self.parm.peek()

    def pop(self): 
        return self.parm.pop()

    def size(self):
        return self.parm.listSize()

    def print(self):
        n = self.parm.listSize()
        for i in range(n-1):
            _tmp = self.parm.get(i)
            coef = _tmp[0]
            order = _tmp[1]
            print("{} x^{} + ".format(coef,order), end = "")
        if self.parm.get(n-1)[1] == 0:
            print(self.parm.get(n-1)[0])
        else:
            print("{} x^{}".format(self.parm.get(n-1)[0], self.parm.get(n-1)[1]))
    @classmethod
    def add(cls,q,p):
        r = Poly()
        while p.size() > 0 and q.size() > 0:
            if p.peek() > q.peek():
                _tep = p.pop()
                r.setParm(_tep[0],_tep[1])
            elif q.peek() > p.peek():
                _tep = q.pop()
                r.setParm(_tep[0],_tep[1])
            else:
                _tep1 = p.pop()
                _tep2 = q.pop()
                r.setParm(_tep1[0]+_tep2[0],_tep1[1])
        if p.size() != 0:
            while p.size() > 0:
                _tep = p.pop()
                r.setParm(_tep[0],_tep[1])
        else:
            while q.size() > 0:
                _tep = q.pop()
                r.setParm(_tep[0],_tep[1])
        return r
            

p = Poly()
p.setParm(4,4)
p.setParm(3,2)
p.print()
q = Poly()
q.setParm(3,3)
q.setParm(4,2)
q.setParm(2,1)
q.setParm(1,0)
q.print()
r = Poly.add(p, q)
r.print()
class Node:
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link

class linked_link:
    def __init__(self):
        self.root = None
    def append(self,item):
        NewNode = None(item)
        if self.root == None:
            self.root = NewNode
        else:
            Curnode = self.root
            while Curnode.link != None:
                Curnode = Curnode.link
            Curnode.link = NewNode

    def insert(self,idx,item):
        NewNode = Node(item)
        CurNode = self.root
        if idx == 0:
            _tmp = self.root
            self.root = NewNode
            NewNode.link = _tmp
        else:
            for i in range(idx-1):
                CurNode = CurNode.link
            _tmp = CurNode.link
            CurNode.link = NewNode
            NewNode.link = _tmp

    def find(self,itme):
        CurNode = self.root
        idx = 0
        while CurNode.link != None:
            if CurNode.itme == item:
                return idx
                break
            else:
                CurNode = CurNode.link
                idx += 1
    
    def delete(self,item):
        CurNode = self.root
        PrevNode = None
        if self.root.item == item:
            self.root == self.root.link
        else:
            while CurNode.item != item:
                PrevNode = CurNode
                CurNode = CurNode.link
                if CurNode.item == item:
                    PrevNode.link = CurNode.link
            if CurNode.item == item:
                PrevNode.link = None
    
    def peek(self):
        return self.root.item[1]
    def pop(self):
        _tmp = self.root
        self.root = _tmp.link
        return _tmp.item
    def get(self,idx):
        curNode = self.root
        for i in range(idx):
            curNode = curNode.link
        return curNode.item


class Poly3:
    def __init__(self):
        #self.parm = []
        self.parm = LinkedList()

    def setParm(self, coef, order):
        self.parm.append([coef, order])

    def peek(self):
        # return order
        #return self.parm[0][1]
        return self.parm.peek()

    def pop(self): 
        # return list 
        #return self.parm.pop(0)
        return self.parm.pop()

    def size(self):
        #return len(self.parm)
        return self.parm.listSize()

    def print(self):
        n = self.parm.listSize()
        for i in range(n-1):
            _tmp = self.parm.get(i)
            coef = _tmp[0]
            order = _tmp[1]
            # coef = self.parm[i][0]
            # order = self.parm[i][1]
            print("%d x^%d + " % (coef, order), end = "")
        if self.parm.get(n-1)[1] == 0:
            print("%d" % self.parm.get(n-1)[0])
        # if self.parm[-1][1] == 0:
        #     print("%d" % self.parm[-1][0])
        else:
            #print("%d x^%d" % (self.parm[-1][0], self.parm[-1][1]))
            print("%d x^%d" % (self.parm.get(n-1)[0], self.parm.get(n-1)[1]))
    @classmethod        
    def add(cls,p,q):
        r = Poly3()
        while p.size() > 0 and q.size() > 0:
            if p.peek() > q.peek():
                _tmp = p.pop()
                r.setParm(_tmp[0],_tmp[1])
            elif p.peek() < q.peek():
                _tmp = q.pop()
                r.setParm(_tmp[0],_tmp[1])
            else:
                _tmp1 = p.pop()
                _tmp2 = q.pop()
                r.setParm(_tmp1[0]+_tmp2[0],_tmp1[1])
        if p.size() == 0:
            while q.size() >0:
                _tmp = q.pop()
                r.setParm(_tmp[0],_tmp[1])
        else:
            while p.size() > 0:
                _tmp = p.pop()
                r.setParm(_tmp[0],_tmp[1])
class DNode:
    def __init__(self,item = None, rlink = None, llink = None):
        self.item = item
        self.rlink = rlink
        self.llink = llink

class DoubleLinkedList:
    def __init__(self):
        self.root = DNode()
        self.current = self.root

    def append(self,item):
        NewNode = DNode(item)
        if self.root.item == None:
            self.root = NewNode
        else:
            CurNode = self.root
            while CurNode.rlink != None:
                CurNode = CurNode.rlink
            CurNode.rlink = NewNode
            NewNode.llink = CurNode

    def setCurrent(self,item):
        CurNode = self.root
        if CurNode.item == item:
            self.current = CurNode
            print("현재 위치는 {}입니다".format(self.current.item))
        else:
            while CurNode.rlink != None:
                CurNode = CurNode.rlink
                if CurNode.item == item:
                    self.current = CurNode
                    print("현재 위치는 {}입니다".format(self.current.item))
    def moveleft(self):
        if self.current == self.root:
            print("처음입니다")
        else:
            self.current = self.current.llink
            print("현재 위치는 {}입니다".format(self.current.item))

    def moveright(self):
        if self.current.rlink == None:
            print("마지막입니다")
        else:
            self.current = self.current.rlink
            print("현재 위치는 {}입니다".format(self.current.item))

    def print(self):
        cur_Node = self.root
        while cur_Node.rlink != None:
            print(cur_Node.item)
            cur_Node = cur_Node.rlink
        print(cur_Node.item)
    
    def listSize(self):
        CurNode = self.root
        count = 1
        if self.root.item == None:
            return 0
        else:
            while CurNode.rlink != None:
                count +=1
                CurNode = CurNode.rlink
            return count

    def get(self,idx):
        return_Node = self.root
        for itr in range(idx):
            return_Node = return_Node.rlink
        return return_Node    

    
    def insert(self,value,idx):
        NewNode = DNode(value)
        if idx == 0:
            tmp = self.root
            self.root = NewNode
            NewNode.rlink = tmp
        else:
            prev_node = self.get(idx-1)
            next_node = prev_node.rlink
            if next_node == None:
                prev_node.rlink = NewNode
                NewNode.llink = prev_node
            else:
                prev_node.rlink = NewNode
                NewNode.llink = prev_node
                NewNode.rlink = next_node
                next_node.llink = NewNode
    def find(self,value):
        CurNode = self.root
        count = 0
        if self.root.item == value:
            print(count)
        else:
            while CurNode.rlink != None:
                CurNode = CurNode.rlink
                count += 1
                if CurNode.item == value:
                    print(count)
    def delete(self,value):
        CurNode = self.root
        if self.root.item == value:
            self.root = self.root.rlink
        else:
            while CurNode.rlink != None:
                CurNode = CurNode.rlink
                if CurNode.item == value:
                    if CurNode.rlink == None:
                        CurNode.llink.rlink = None
                    else:
                        CurNode.llink.rlink = CurNode.rlink            


            

fruits = DoubleLinkedList()
fruits.append("사과")
fruits.append("오렌지")
fruits.append("배")
fruits.insert("수박", 3)
fruits.print()
# fruits.find("배")
fruits.delete("수박")
fruits.print()
# fruits.setCurrent("오렌지")
# fruits.moveright()
# print(fruits.listSize())
class Node:
    def __init__(self, item = None, link = None): 
        self.item = item
        self.link = link

class LinkedList:
    def __init__(self):
        self.root = None
    def append(self,item):
        new_Node = Node(item)
        if self.root == None:
            self.root = new_Node
        else:
            cur_Node = self.root
            while cur_Node.link != None:
                cur_Node = cur_Node.link
            cur_Node.link = new_Node
    def print(self):
        cur_Node = self.root
        while cur_Node.link != None:
            print(cur_Node.item)
            cur_Node = cur_Node.link
        print(cur_Node.item)

    def listSize(self):
        if self.root == None:
            return(0)
        size = 1
        cur_Node = self.root
        while cur_Node.link != None:
            size += 1
            cur_Node = cur_Node.link
        return(size)
    def get(self,idx):
        return_Node = self.root
        for itr in range(idx):
            return_Node = return_Node.link
        return return_Node

    def insert(self,idx,item):
        new_Node = Node(item)
        if idx == 0:
            tmp = self.root
            self.root = new_Node
            new_Node.link = tmp
        else:
            prev_Node = self.get(idx)
            next_Node = prev_Node.link
            prev_Node.link = new_Node
            new_Node.link = next_Node


    def find(self,item):
        find = -1
        i = 0
        if self.root.item == item:
            find += 1
        else:
            cur_Node = self.root
            while cur_Node.link != None:
                cur_Node = cur_Node.link
                i += 1
                if cur_Node.item == item:
                    find = i
                    break
        print(find) 
    def delete(self,item):
        i = 0
        prev_Node = None
        if self.root.item == item:
            self.root = self.root.link
        else:
            cur_Node = self.root
            while cur_Node.link != None:
                prev_Node = cur_Node
                cur_Node = cur_Node.link
                if cur_Node.item == item:
                    prev_Node.link = cur_Node.link


    


a=LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.insert(0,5)
# a.listSize()
a.print()
# a.find(4)

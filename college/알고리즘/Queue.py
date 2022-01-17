from Node_structure import Node
from Stack import Stack
class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None
    def enqueue(self,item):
        new_Node = Node(item,None)
        if self.size == 0:
            self.front = new_Node
        else:
            self.rear.next = new_Node
        self.rear = new_Node
        self.size +=1
    def dequeue(self):
        if self.size != 0:
            fitem = self.front.item
            self.front = self.front.next
            self.size -= 1
            if self.size == 0:
                self.rear = None
            return fitem
    def print_que(self):
        p = self.front
        print("front: ",end="")
        while p:
            if p.next != None:
                print(p.item,"-> ",end="")
            else:
                print(p.item,end="")
            p = p.next
        print(" : rear")
# q = Queue()
# q.enqueue("apple")
# q.enqueue("orange")
# q.enqueue("cherry")
# q.enqueue("pear")
# q.print_que()
# q.dequeue()
# q.print_que()

def pallndrome(str):
    q = Queue()
    s = Stack()
    str_list = list(str)
    q_list = []
    s_list = []
    for i in range(len(str_list)):
        q.enqueue(str_list[i])
        s.push(str_list[i])
    for i in range(len(str_list)):
        q_list.append(q.dequeue())
        s_list.append(s.pop())
    print("".join(q_list))
    print("".join(s_list))
    if q_list == s_list:
        return (True)
    else:
        return(False)

# print(pallndrome("WOWq"))


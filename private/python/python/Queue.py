from single_linked_list import SinglyLinkedList 

class Queue(object):
    lstinstance = SinglyLinkedList()
    def dequeue(self):
        return self.lstinstance.removeAt(0)
    def enqueue(self,value):
        self.lstinstance.insertAt(value,self.lstinstance.getSize())


queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print( queue.dequeue())
print( queue.dequeue())
print( queue.dequeue())
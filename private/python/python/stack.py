from single_linked_list import SinglyLinkedList 

class Stack(object):
    lstinstance = SinglyLinkedList()
    def pop(self):
        return self.lstinstance.removeAt(0)
    def push(self,value):
        self.lstinstance.insertAt(value,0)

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

print (stack.pop())
print (stack.pop())
print (stack.pop())
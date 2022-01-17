class Stack:
    def __init__(self):
        self.s = []
    def push(self,item):
        self.s.append(item)
    def isEmpty(self):
        return len(self.s) == 0
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

def reverse(a):
    s = Stack()
    b = ""
    for i in range(len(a)):
        s.push(a[i])
    for i in range(len(a)):
        b += s.pop()
    return b
a = "abcdefg"
print(reverse(a))

class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

    def isEmpty(self):
        if len(self.s) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.s)

    def print(self):
        print(self.s)

class Queue:
    def __init__(self):
        self.q = []

    def enQueue(self, item):
        self.q.append(item)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.q.pop(0)

    def size(self):
        return len(self.q)

    def isEmpty(self):
        if len(self.q) > 0:
            return False
        else:
            return True

    def peek(self):
        if self.isEmpty() == False:
            return self.q[0]

    def delete(self, item):
        if item in self.q:
            self.q.remove(item)
        else:
            print("해당 아이템이 존재하지 않습니다.")


class Graph:
    def __init__(self,graph,start):
        self.graph = graph
        self.start = start
        self.s = Stack()
        self.q = Queue()
        self.visit = []

    def dfs(self):
        self.s.push(self.start)
        while self.s.isEmpty() == False:
            curNode = self.s.pop()
            if curNode not in self.visit:
                self.visit.append(curNode)
                for node in sorted(list(set(self.graph[curNode])-set(self.visit))):
                    self.s.push(node)
    
    def bfs(self):
        visit = [self.start]
        for item in self.graph[self.start]:
            self.q.enQueue(item)
        
        while self.q.isEmpty() == False:
            item = self.q.deQueue()
            if not item in visit:
                for _item in self.graph[item]:
                    self.q.enQueue(_item)
                visit.append(item)
        return visit

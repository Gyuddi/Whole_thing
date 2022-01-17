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

def bfs(dict, start):
    q = Queue()
    visited = [start]
    for item in dict[start]:
        q.enQueue(item)
    while q.isEmpty() == False:
        item = q.deQueue()
        if not item in visited:
            for _item in dict[item]:
                q.enQueue(_item)
            visited.append(item)
    return visited

fr_info={'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
# print(bfs(fr_info,"Summer"))
def dfs(dict,start,visited =[]):
    visited.append(start)
    if start not in dict.keys():
        return None     
    for node in dict[start]:
        if node not in visited:
            dfs(dict,node,visited)
    return visited
    
print(dfs(fr_info,"ICN"))
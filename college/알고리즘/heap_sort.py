import random
class max_heap:
    def __init__(self):
        self.x = [None]

    def _exchange(self,i,j):
        if self.x[i] < self.x[j]:
            self.x[i],self.x[j] =  self.x[j],self.x[i]
    
    def push(self, item):
        self.x.append(item)
        cIndex = len(self.x) -1
        pIndex = cIndex // 2
        while pIndex >= 1:
            self._exchange(pIndex,cIndex)
            cIndex = pIndex
            pIndex = cIndex//2
    def pop(self):
        item = self.x[1]
        n = len(self.x) -1
        self.x[1], self.x[n] = self.x[n], self.x[1]
        self.x = self.x[:-1]
        self.heapify()
        return item
    def _child(self,pIndex):
        n = len(self.x)
        leftIndex = pIndex * 2
        rightIndex = pIndex * 2 +1
        if rightIndex <= n-1:
            return leftIndex,rightIndex
        elif leftIndex == n-1:
            return leftIndex, None
        else:
            return None,None
    def heapify(self):
        pIndex = 1
        lastIndex = len(self.x) -1
        while pIndex < len(self.x):
            left,right = self._child(pIndex)
            if left != None and right == None:
                self._exchange(pIndex, left)
            elif left != None and right != None:
                if self.x[left] > self.x[right]:
                    self._exchange(pIndex,left)
                else:
                    self._exchange(pIndex,right)
            pIndex += 1
    def h_print(self):
        print(self.x)

    def heap_sort(self):
        answer = []
        for i in range(len(self.x)-1):
            answer.append(self.pop())
        return answer

a = max_heap()

for i in range(100):
    num = random.randrange(1,5000)
    a.push(num)
print(a.heap_sort())
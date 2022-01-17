import numpy as np
class minHeap:
    def __init__(self):
        self.x = [None]
        
    def _exchange(self,i,j):
        if self.x[i] > self.x[j]:
            self.x[i],self.x[j] =  self.x[j],self.x[i]
        
    def push(self, item):
        self.x.append(item) 
        cIndex = len(self.x) - 1
        pIndex = cIndex // 2
        while pIndex >= 1:
            self._exchange(pIndex, cIndex)
            cIndex = pIndex
            pIndex = cIndex // 2
   
    def pop(self):
        item = self.x[1]
        n = len(self.x) - 1
        self.x[1], self.x[n] = self.x[n], self.x[1]
        self.x = self.x[:-1]
        self.heapify()
        return item
    
    def _child(self, pIndex):
        n = len(self.x)
        leftIndex = pIndex * 2
        rightIndex = pIndex * 2 + 1
        if rightIndex <= n-1: 
            return leftIndex, rightIndex
        elif leftIndex == n-1:
            return leftIndex, None
        else:
            return None, None
        
    def heapify(self):
        pIndex = 1
        lastIndex = len(self.x) - 1
        while pIndex < len(self.x):
            left, right = self._child(pIndex)
            if left != None and right == None :
                self._exchange(pIndex, left)
            elif left != None and right != None:
                if self.x[left] > self.x[right]:
                    self._exchange(pIndex, right)
                else:
                    self._exchange(pIndex, left)
            pIndex += 1
            
    def print(self):
        print(self.x)

stock = minHeap()
# mouse_price = round(np.random.normal(10000, 1000))
for i in range(10):
    stock.push(round(np.random.normal(10000, 1000)))
stock.print()

# for i in range(10):
#     print(stock.pop())
# sold_out = []
# while True:
#     sold = stock.pop()
#     sold_out.append(sold-7000)
#     stock.push(round(np.random.normal(10000, 1000)))
#     if len(sold_out) > 20:
#         break
# print(sold_out)
# print(np.mean(sold_out))    
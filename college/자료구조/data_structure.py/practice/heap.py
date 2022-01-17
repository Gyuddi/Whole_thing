class maxHeap:
    def __init__(self):
        self.x = [None]
    
    def _exchange(self,i,j):
        if self.x[i] < self.x[j]:
            self.x[i],self.x[j] =  self.x[j],self.x[i]
    def push(self, item):
        self.x.append(item)
        cindex = len(self.x) -1
        pindex = cindex // 2
        while pindex >=1:
            self._exchange(pindex,cindex)
            cindex = pindex
            pindex = cindex //2
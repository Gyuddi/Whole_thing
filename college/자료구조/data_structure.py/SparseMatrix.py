class SparseMatrix:
    def __init__(self,m,n):
        self.s = [[m, n, 0]]
        self.m = m
        self.n = n
        
    def append(self,i,j,val):
        if val != 0:
            self.s.append([i,j,val])
        self.s[0][2] += 1
    def shape(self):
        return (self.m,self.n)
    def getValue(self,i,j):
        for k in range(1,len(self.s)):
            if self.s[k][0] == i and self.s[k][1] == j:
                return self.s[k][2]
        return 0
    def write_down(self):
        import numpy as np
        _tmp = np.zeros((self.m,self.n))
        for i in range(1,len(self.s)):
            _tmp[self.s[i][0]-1,self.s[i][1]-1] = self.s[i][2]
        print(_tmp)
    @classmethod
    def add(cls, p, q):
        if p.m != q.m or p.n != q.n:
            return -1
        r = SparseMatrix(p.m, p.n)
        u = set()
        for i in range(1, len(p.s)):
            u.add((p.s[i][0], p.s[i][1]))
        for i in range(1, len(q.s)):
            u.add((q.s[i][0], q.s[i][1]))
        for term in list(u):
            _tmp = p.getValue(term[0], term[1]) + q.getValue(term[0], term[1])
            if _tmp != 0:
                r.append(term[0], term[1], _tmp)
        return r
    @classmethod
    def mult(cls,p,q):
        if p.m != q.m or p.n != q.n:
            return -1
        r = SparseMatrix(p.m, p.n)
        for i in range(1,p.m+1):
            for j in range(1,q.n+1):
                _tmp = 0
                for k in range(1,p.n+1):
                    _tmp += p.getValue(i,k) * q.getValue(k,j)
                if _tmp != 0:
                    r.append(i, j, _tmp)
        return r



a = SparseMatrix(3,3)
b = SparseMatrix(3,3)

a.append(1,1,1)
a.append(2,2,2)
a.append(3,3,3)
b.append(1,1,4)
b.append(1,2,7)
b.append(2,3,2)
b.append(3,3,1)

a.write_down()
b.write_down()

# print(a.getValue(3,3))

c = SparseMatrix.mult(a, b)
c.write_down()

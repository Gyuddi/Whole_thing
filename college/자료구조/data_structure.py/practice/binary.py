class BNode:
    def __init__(self, item):
        self.item=item
        self.left = None
        self.right = None
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node   


class BinaryTree:
    def __init__(self,root):
        self.root = root
    
    def preOrder(self,n):
        print(n.item," ",end=" ")
        if n.left:
            self.preOrder(n.left)
        if n.right:
            self.preOrder(n.right)
    
    def inOrder(self, n):
        if n.left: self.inOrder(n.left)
        print(n.item,' ', end=' ')
        if n.right: self.inOrder(n.right)

    def postOrder(self, n):
        if n.left: self.postOrder(n.left)
        if n.right: self.postOrder(n.right)    
        print(n.item,' ', end=' ')
    
    def height(self, n):
        # 특정 노드에서 왼쪽으로 끝까지 가보고, 오른쪽으로 끝까지 가보고 ...
        if n is None:
            return 0
        else:
            lheight = self.height(n.left)
            rheight = self.height(n.right)
            # 각 노드별로 끝이 됐을 때, 리 턴값을 프린트한다.
            print(n.item, lheight + 1, rheight + 1)
            # Use the larger one
            # 루트 노드가 맨 마지막에 리턴된다.
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
    def levelOrder(self):
        h = self.height(self.root)
        for i in range(1,h+1):
            self._levelOrder(self.root,i)
            print()
    def _levelOrder(self,node,level):
        if node is None:
            return
        if level == 1:
            print(node.item,end=" ")
        elif level > 1 :
            self._levelOrder(node.left, level -1)
            self._levelOrder(node.right, level -1)
a = BNode('A')
b = BNode('B')
c = BNode('C')
d = BNode('D')
e = BNode('E')
f = BNode('F')
g = BNode('G')
h = BNode('H')
i = BNode('I')
j = BNode('J')
k = BNode('K')

a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)
c.setLeft(f)
c.setRight(g)
d.setLeft(h)
e.setLeft(i)
e.setRight(j)
g.setRight(k)

bt = BinaryTree(a)
bt.height(a)
class BNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BSTree:
    def __init__(self):
        self.root = None
    def insert(self,item):
        self.root = self._insert(self.root,item)
    def _insert(self,curNode,item):
        if curNode == None:
            curNode = BNode(item)
        elif item < curNode.item:
            curNode.left = self._insert(curNode.left, item)
        else:
            curNode.right = self._insert(curNode.right, item)    
        return curNode
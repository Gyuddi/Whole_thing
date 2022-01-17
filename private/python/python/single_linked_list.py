from Node import Node


class   ():
    nodeHead = ""
    nodeTail = ""
    size = 0
    def __init__(self):
        self.nodeTail = Node(binTail=True)
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)

    def insertAt(self,objInsert,idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert-1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size +1
    
    def removeAt(self,idxRemove):
        nodePrev = self.get(idxRemove-1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size -1
        return nodeRemove.getValue()

    def get(self,idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail == False:
            nodeCurrent = nodeCurrent.getNext()
            print (nodeCurrent.getValue())
        
        
        
    def getSize(self):
        return self.size
        

list1 = SinglyLinkedList()
list1.insertAt("A",0)
list1.insertAt("B",1)
list1.insertAt("D",2)
list1.insertAt("E",3)
list1.insertAt("F",4)
list1.printStatus()

list1.insertAt("C",2)
list1.printStatus()

list1.removeAt(3)
list1.printStatus()

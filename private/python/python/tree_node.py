class TreeNode:
    nodeLMS = ""
    nodePMS = ""
    nodeParent = ""
    value = ""
    root = ""

    def __init__(self,value,nodeParent):
        self.value = value
        self.nodeParent = nodeParent
    def getLMS(self):
        return self.nodeLMS
    def getRMS(self):
        return self.nodeRMS
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent
    def setLMS(self,LMS):
        self.nodeLHS = LMS
    def setRMS(self,RMS):
        self.nodeRMS = RMS
    def setValue(self,value):
        self.value = value
    def setParent(self,nodeParent):
        self.nodeParent = nodeParent
    def insert(self,value,node = ""):
        if node == "":
            node = self.root
        if self.root == "":
            self.root = TreeNode(valus, "")
            return
        if value == node.getValue():
            if node.getRMS() == "":
                node.setRMS(TreeNode(value,node))
            else:
                self.insert(value, node.getRMS())
        if value < node.getValue():
            if node.getLMS() == "":
                node.setLMS(TreeNode(value,node))
            else:
                self.insert(value, node.getLMS())
        return
    def search(self,value,node = ""):
        if node == "":
            node = self.root
        if value == node.getValue():
            return True
        if value > node.getValue():
            if node.getRMS() == "":
                return False
            else:
                return self.search(value,node.getRMS())
        if value < node.getValue():
            if node.getLMS() == "":
                return False
            else:
                return self.search(value,node.getLMS())



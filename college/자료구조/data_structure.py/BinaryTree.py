import math
class BinaryTree:
    def __init__(self):
        self.t = [None]
        
    def append(self, item):
        self.t.append(item)
    
    def size(self):
        return len(self.t) - 1
    
    def getChild(self, item):
        if item in self.t:
            k = self.t.index(item)
            lidx = 2 * k
            ridx = 2 * k + 1
            if lidx <= self.size():
                lnode = self.t[lidx]
            else:
                lnode = None
            if ridx <= self.size():
                rnode = self.t[ridx]
            else:
                rnode = None    
            return lnode, rnode
        else:
            print('item not found~')
    
    def getParent(self, item):
        if item in self.t:
            k = self.t.index(item)
            pidx = k // 2
            if pidx > 0:
                return self.t[pidx]
            else:
                return None
        else:
            print('item not found~')

    def find_dis(self,item1,item2):
        if item1 == item2:
            # print(self.size()-self.t.index(item1))
            h = int(math.log(self.size(),2))
            i = int(math.log(self.t.index(item1),2))
            print(item1,"질병 간 거리 ={}/{}".format(h-i,h))
        elif item1 == None or item2 == None:
            print("거리를 계산할 수 없습니다.")
        else:
            self.find_dis(self.getParent(item1), self.getParent(item2))
            
        
            
tree = BinaryTree()
disease = ["호흡기/소화기병","호흡기병","소화기병","호흡기감염","폐질환","위질환","결장질환","독감","기관지염","폐부종","폐색전증","위궤양","위암","대장염","대장암"]
for i in disease:
    tree.append(i)
tree.find_dis("대장암","독감")

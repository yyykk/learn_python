from queue import Queue

class Tree:
    Counter = 0
    def __init__(self, val = '#', left = None, right = None):
        self.val = val
        self.counter = 0
        self.left = left
        self.right = right
        self.ponit = None
        self.father = None
        Tree.Counter += 1

    
    #∂—≈≈–Ú
    def HeadSort(self, List):
         for i in range(len(List)):
            self.BuildHeadTree(List[i])
           
    def GetPoint(self):
        dec = int((self.counter + 1) / 2)
        road = str(bin(dec))[3:]
        p = self
        for r in road:
            if (r == '0'):
                p = p.left
            else:
                p = p.right
        return p

    def BuildHeadTree(self, val):
        print('val = ', val, 'self.counter = ', self.counter)
        self.ponit = self.GetPoint()
        print('self.ponit.val = ', self.ponit.val)  
        if (self.counter == 0):
            self.val = val
            self.father = self
        else:
            node = Tree(val)
            node.father = self.ponit
            if(self.counter % 2 == 0):
                self.ponit.left = node
            else:
                self.ponit.right = node
            temp = self.counter
            while(temp != 0):
                if (node.val < node.father.val):
                    if (temp == self.counter):
                        self.ponit = node.father
                    if (int(temp / 2) % 2 == 0):
                        node.father.father.left = node
                    else:
                        node.father.father.right = node
                    if(temp % 2 == 0):
                        node.left = node.father
                    else:
                        node.left = node.father.left
                        node.right = node.father
                    node.father = node.father.father
                    temp = int(temp / 2)
                    print('node,val = ', node.val, 'node,father.val = ', node.father.val)
                else:
                    break;
        self.counter += 1
        print('Tree = ')
        self.VisitNode()
                       
                


    #«∞–Ú±È¿˙∂˛≤Ê ˜
    def VisitNode(self):
        print(self.val)
        if(self.left != None):
            self.left.VisitNode()
        if(self.right != None):
            self.right.VisitNode()

if __name__ == '__main__':
    root = Tree()
    number = [2, 5, 4, 3, 1]
    root.HeadSort(number)
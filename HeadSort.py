from queue import Queue

class Tree:
    def __init__(self, val = '#', left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.ponit = None
        self.father = None
        self.counter = 0 


    #前序构建二叉树
    def FrontBuildTree(self):
        temp = input('Please Input: ')
        node = Tree(temp)
        if(temp != '#'):
            node.left = self.FrontBuildTree()
            node.right = self.FrontBuildTree()
        return node#因为没有引用也没有指针，所以就把新的节点给返回回去
    
    #堆排序
    def HeadSort(self, List):
        for val in List:
            print('val = ', val, 'self.counter = ', self.counter)
            self.ponit = self.GetPoint()
            print('self.ponit.val = ', self.ponit.val)  
            if (self.counter == 0):
                self.val = val
                self.father = self
            else:
                temp = self.counter + 1
                node = Tree(val)
                node.father = self.ponit
                if(temp % 2 == 0):
                    self.ponit.left = node
                else:
                    self.ponit.right = node
                while(temp != 0):
                    if (node.val < node.father.val):
                        p = node.father
                        LeftTemp = node.left
                        RightTemp = node.right
                        if (p.father != p):
                            if (int(temp / 2) % 2 == 0):
                                p.father.left = node
                            else:
                                p.father.right = node
                            node.father = p.father
                        else:
                            node.father = node
                            node.counter = self.counter
                            self = node 
                        if(temp % 2 == 0):
                            node.left = p
                            node.right = p.right
                            if (p.right != None):
                                p.right.father = node
                        else:
                            node.left = p.left
                            node.right = p
                            if (p.left != None):
                                p.left.father = node
                        p.left = LeftTemp
                        p.right = RightTemp
                        p.father = node
                        temp = int(temp / 2)
                        print('node.val = ', node.val, 'node.father.val = ', node.father.val)
                        print('Tree = ')
                        self.VisitNode()
                    else:
                        break;
            self.counter += 1
        return self
           
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
            temp = self.counter + 1
            node = Tree(val)
            node.father = self.ponit
            if(temp % 2 == 0):
                self.ponit.left = node
            else:
                self.ponit.right = node
            while(temp != 0):
                if (node.val < node.father.val):
                    p = node.father
                    LeftTemp = node.left
                    RightTemp = node.right
                    if (p.father != p):
                        if (int(temp / 2) % 2 == 0):
                            p.father.left = node
                        else:
                            p.father.right = node
                        node.father = p.father
                    else:
                        node.father = node
                        node.counter = self.counter
                        self = node 
                    if(temp % 2 == 0):
                        node.left = p
                        node.right = p.right
                    else:
                        node.left = p.left
                        node.right = p
                    p.left = LeftTemp
                    p.right = RightTemp
                    p.father = node
                    temp = int(temp / 2)
                    print('node,val = ', node.val, 'node,father.val = ', node.father.val)
                    print('Tree = ')
                    self.VisitNode()
                else:
                    break;
        self.counter += 1
                       
                


    #前序遍历二叉树
    def VisitNode(self):
        print(self.val)
        if(self.left != None):
            self.left.VisitNode()
        if(self.right != None):
            self.right.VisitNode()

if __name__ == '__main__':
    root = Tree()
    number = [3, 5, 4, 3, 1, 6, 9]

    root = root.HeadSort(number)
    root.VisitNode()   
    #root = root.FrontBuildTree()
    #root.VisitNode()
        
        
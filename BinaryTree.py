class Tree:
    def __init__(self, val = '#', left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    #ǰ�򹹽�������
    def FrontBuildTree(self):
        temp = input('Please Input: ')
        node = Tree(temp)
        if(temp != '#'):
            node.left = self.FrontBuildTree()
            node.right = self.FrontBuildTree()
        return node#��Ϊû������Ҳû��ָ�룬���ԾͰ��µĽڵ�����ػ�ȥ
    
    #ǰ�����������
    def VisitNode(self):
        print(self.val)
        if(self.val != '#'):
            self.left.VisitNode()
            self.right.VisitNode()

if __name__ == '__main__':
    root = Tree()
    root = root.FrontBuildTree()
    root.VisitNode()
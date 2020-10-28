class node:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild: node = lchild
        self.rchild: node = rchild


class Cstack:

    def __init__(self):
        self.stack = []

    def pop(self):
        self.stack.pop(-1)

    def push(self, i):
        self.stack.append(i)

    def returntop(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)


class btree:

    def __init__(self):
        self.root = None
        self.SQlist = []

    def PreorderCreatTree(self, data):
        Node = node(data)
        if self.root == None:
            self.root = Node
            self.SQlist.append(Node)
        else:
            rootNode = self.SQlist[0]
            if rootNode.lchild == None:
                rootNode.lchild = Node
                self.SQlist.append(rootNode.lchild)
            elif rootNode.rchild == None:
                rootNode.rchild = Node
                self.SQlist.append(rootNode.rchild)
                self.SQlist.pop(0)

    def LayerCreatTree(self, data: list):

        if self.root == None:

            Node = node(data[0])

            self.root = Node

            self.SQlist.append(Node)

        else:
            while (data != []):
                rootNode = self.SQlist[0]
                NodeL = node(data[0])
                NodeR = node(data[1])
                rootNode.lchild = NodeL
                rootNode.rchild = NodeR
                self.SQlist.pop(0)
                data.pop(0)
                data.pop(0)
                self.SQlist.append(NodeL)
                self.SQlist.append(NodeR)

    def MathCreatTree(self, string: str):
        stack = []
        Pre_Root_Node = None
        DIR = True
        for op in range(0, len(string)):
            if string[op] == "(":
                DIR = True
                stack.append(Pre_Root_Node)
            elif string[op] == ")":
                stack.pop(-1)
            elif string[op] == ",":
                DIR = False
            else:
                Pre_Root_Node = node(string[op])
                if self.root == None:
                    self.root = Pre_Root_Node
                else:
                    if DIR:
                        stack[-1].lchild = Pre_Root_Node
                    else:
                        stack[-1].rchild = Pre_Root_Node

    def traverse(self, Node: node):
        if not Node.lchild and not Node.rchild:
            return [str(Node.data)]
        left, right = [], []
        if Node.lchild:
            left = [str(Node.data) + x for x in self.traverse(Node.lchild)]
        if Node.rchild:
            right = [str(Node.data) + x for x in self.traverse(Node.rchild)]
        return left + right

    # def Find_Path(self, Node: node):
    #     if not Node.lchild and not Node.rchild:
    #         return [Node.data]
    #     left, right = [], []
    #     if Node.lchild:
    #         left = [Node.data + i for i in self.Find_Path(Node.lchild)]
    #     if Node.rchild:
    #         right = [Node.data + i for i in self.Find_Path(Node.rchild)]
    #     return left + right

    def PreOrderTraverse(self, root):
        if root == None:
            return None
        else:
            print(root.data, end=' ')
            self.PreOrderTraverse(root.lchild)
            self.PreOrderTraverse(root.rchild)

    def MidOrderTraverse(self, root):
        if (root == None):
            return None
        else:
            self.PreOrderTraverse(root.lchild)
            print(root.data, end=' ')
            self.PreOrderTraverse(root.rchild)

    def RearOrderTraverse(self, root):
        if (root == None):
            return None
        else:
            self.PreOrderTraverse(root.lchild)
            self.PreOrderTraverse(root.rchild)
            print(root.data, end=' ')

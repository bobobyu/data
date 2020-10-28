class node:
    def __init__(self, name: str = None, value: int = None):
        self.name: str = name
        self.value: int = value
        self.lchild: node = None
        self.rchild: node = None


HF_dic: dict = {'templatetags': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 3}


class HF_tree:
    def __init__(self, dic: dict):
        self.list: list = [node(i, dic[i]) for i in list(dic.keys())]
        while len(self.list) > 1:
            self.list.sort(key=lambda x: x.value)
            New_root: node = node(value=self.list[0].value + self.list[1].value)
            New_root.lchild = self.list[0]
            New_root.rchild = self.list[1]
            self.list.append(New_root)
            [self.list.pop(0) for _ in range(2)]
        self.root: node = self.list[-1]

    lis: list = []

    def show_weight(self, root_node: node, name: str, height: int = 0):
        if root_node:
            if root_node.name == name:
                HF_tree.result = height
                tree.lis.append(height)
            self.show_weight(root_node.lchild, name, height + 1)
            self.show_weight(root_node.rchild, name, height + 1)



tree = HF_tree(HF_dic)
tree.show_weight(tree.root, 'templatetags', 1)
tree.show_weight(tree.root, 'b', 1)
tree.show_weight(tree.root, 'e', 1)
print(tree.lis)

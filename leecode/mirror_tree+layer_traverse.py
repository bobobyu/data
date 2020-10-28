class Node:
    def __init__(self, value):
        self.value = value
        self.lchild: Node = None
        self.rchild: Node = None


class Tree:

    def __init__(self, value_list: list):
        self.value_list: list = value_list
        self.value_list_copy: list = value_list[:]
        self.root_node: Node = Node(value=None)
        self.value_stack: list = []
        self.layer_: list = []


    def generate_tree(self):

        while len(self.value_list):
            if not self.value_stack:
                self.root_node.value = self.value_list.pop(0)
                self.value_stack.append(self.root_node)
            else:
                lnode = Node(value=self.value_list.pop(0))
                rnode = Node(value=self.value_list.pop(0))
                self.value_stack[0].lchild = lnode
                self.value_stack[0].rchild = rnode
                self.value_stack.append(lnode)
                self.value_stack.append(rnode)
                self.value_stack.pop(0)

    def pre_traverse_tree(self, current_node: Node):
        print(current_node.value)
        if current_node.lchild:
            self.pre_traverse_tree(current_node=current_node.lchild)
        if current_node.rchild:
            self.pre_traverse_tree(current_node=current_node.rchild)

    def search_path(self, current_node: Node, direction: bool) -> list:
        if not current_node.lchild and not current_node.rchild:
            return [current_node.value]
        return [current_node.value] + self.search_path(
            current_node=current_node.lchild if direction else current_node.rchild, direction=direction)

    def judge_mirror_list(self, list_: list):
        while list_:
            if list_.pop(0) != list_.pop(-1):
                return False
        return True

    def judge_mirror_tree(self, current_node: Node) -> bool:
        layer_list: list = []
        sequence_list: list = [self.root_node]
        while sequence_list[0].lchild:
            for i in range(len(sequence_list)):
                layer_list.append(sequence_list[0].lchild.value)
                layer_list.append(sequence_list[0].rchild.value)
                sequence_list.append(sequence_list[0].lchild)
                sequence_list.append(sequence_list[0].rchild)
                sequence_list.pop(0)
            if not self.judge_mirror_list(layer_list):
                return False
            layer_list.clear()
        return True

    def judge_m(self, sequence: list = []) -> bool:
        if not sequence:
            return self.judge_m(sequence=[self.root_node.lchild, self.root_node.rchild])
        else:
            layer_list: list = []
            for i in sequence:
                layer_list.append(i.value)
            if not self.judge_mirror_list(layer_list):
                return False
            elif not sequence[0].lchild:
                return True
            else:
                sequence_ = []
                for i in sequence:
                    sequence_.append(i.lchild)
                    sequence_.append(i.rchild)
                return self.judge_m(sequence=sequence_)


    def traverse_layer(self, sequence: list = []):

        if not sequence:
            return self.traverse_layer(sequence=[self.root_node])
        else:
            layer_list: list = []
            for i in sequence:
                if i.value:
                    layer_list.append(i.value)
            self.layer_.append(layer_list)
            if sequence[0].lchild:
                next_sq = []
                for i in sequence:
                    next_sq.append(i.lchild)
                    next_sq.append(i.rchild)
                self.traverse_layer(sequence=next_sq)

a = Tree(value_list=[1, 2, 2, 3, 4, 4, 4])
a.generate_tree()

# a.pre_traverse_tree(current_node=a.root_node)
# print(a.judge_mirror_tree(current_node=a.root_node))
# print(a.judge_m())
a.traverse_layer()
print(a.layer_)

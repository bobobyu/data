class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.next:TreeNode = None

class Tree:
    def __init__(self, value_list: list):
        stack: list = []
        if value_list:
            while value_list:
                if not stack:
                    self.root_node = TreeNode(value_list.pop(0))
                    stack.append(self.root_node)
                else:
                    left_value = value_list.pop(0)
                    if left_value:
                        left_node = TreeNode(left_value)
                        stack.append(left_node)
                        stack[0].left = left_node
                    if value_list:
                        right_value = value_list.pop(0)
                        if right_value:
                            right_node = TreeNode(right_value)
                            stack.append(right_node)
                            stack[0].right = right_node
                    stack.pop(0)
        else:
            self.root_node = TreeNode(None)

    def preorder(self, current_node: TreeNode):
        if current_node:
            print(current_node.val)
            self.preorder(current_node=current_node.left)
            self.preorder(current_node=current_node.right)

    def pre_order(self):
        self.preorder(current_node=self.root_node)

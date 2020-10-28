from Tree import *


class Solution:
    def __init__(self):
        self.order_stack: list = []
        self.result_list: list = []
    def levelOrder_(self, root: TreeNode):
        if root.val:
            self.result_list.append([root.val])
            self.order_stack.append(root.left)
            self.order_stack.append(root.right)
            while self.order_stack:
                self.result_list.append([i.val for i in self.order_stack if i.val])
                iter_times = len(self.order_stack)
                for i in range(iter_times):
                    if self.order_stack[0].left:
                        self.order_stack.append(self.order_stack[0].left)
                    if self.order_stack[0].right:
                        self.order_stack.append(self.order_stack[0].right)
                    self.order_stack.pop(0)
            return self.result_list
        return []

    def level_Order(self, layer_list: list):
        if layer_list:
            self.result_list.append([i.val for i in layer_list if i.val!=None])
            layer_list_ = []
            for i in layer_list:
                if i.left:
                    layer_list_.append(i.left)
                if i.right:
                    layer_list_.append(i.right)
            self.level_Order(layer_list_)

    def levelOrder(self, root):
        if root:
            self.level_Order(layer_list=[root])
            return self.result_list
        return []

    def levelOrderBottom(self, root: TreeNode):
        if root:
            self.level_Order(layer_list=[root])
            return self.result_list.reverse()
        return []

a = Tree([3,9,20,None,None,15,7])
x = Solution()
x.levelOrder(root=a.root_node)
print(x.result_list)
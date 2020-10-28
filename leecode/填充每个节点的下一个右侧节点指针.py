from Tree import TreeNode as Node
from Tree import Tree
import this

class Solution:
    def connect(self, root: Node) -> Node:
        head_root = root
        def layer_order(head_root: Node):
            stack: list = [head_root]
            while stack:
                if len(stack) > 1:
                    for i in range(len(stack) - 1):
                        stack[i].next = stack[i + 1]
                next_stack: list = []
                while stack:
                    current_node = stack.pop(0)
                    if current_node.left:
                        left_node = current_node.left
                        right_node = current_node.right
                        next_stack.append(left_node)
                        next_stack.append(right_node)
                    else:
                        break
                stack = next_stack
        layer_order(head_root=root)
    def show(self, head)->None:
        def dp(root:Node):
            disp_node = root
            while disp_node:
                print(disp_node.val)
                if disp_node.next:
                    disp_node = disp_node.next
                else:
                    break
            if root.left:
                dp(root.left)
        dp(head)
T = Tree([1,2,3,4,5,6,7])
T.pre_order()
print()
s = Solution()
s.connect(T.root_node)
s.show(T.root_node)


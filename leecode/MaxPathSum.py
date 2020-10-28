from Tree import *


class Solution:
    def recursion(self, node: TreeNode):
        if not node: return 0
        left = self.recursion(node=node.left)
        right = self.recursion(node=node.right)
        self.maxpath = max(self.maxpath, left + right + node.val)
        return max(0, max(left, right) + node.val)

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxpath: float = float('-inf')
        self.recursion(root)
        return int(self.maxpath)

a = Tree([1,2,3])
b = Solution()
print(b.maxPathSum(a.root_node))
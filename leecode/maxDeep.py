from Tree import *

class Solution:
    def __init__(self):
        self.maxdepth: int = 0
    def maxDepth(self, root: TreeNode) -> int:
        self.MaxDepth(root=root)
        return self.maxdepth

    def MaxDepth(self, root: TreeNode, depth: int = 1) -> int:
        if not root or root.val==None:
            return 0
        if root:
            if root.left:
                self.MaxDepth(root.left, depth + 1)
            if root.right:
                self.MaxDepth(root.right, depth + 1)
            if not root.left and not root.right:
                if self.maxdepth <= depth:
                    self.maxdepth = depth

    def maxDepth_(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0
        left_high = self.maxDepth(root.left)
        right_high = self.maxDepth(root.right)
        return max(left_high, right_high) + 1

t = Tree([0,1,2,3])
a = Solution()
# t.pre_order()
a.maxDepth_(root=t.root_node)
print(a.maxdepth)
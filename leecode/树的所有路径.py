from Tree import *

def SearchAllPath(root: TreeNode)->list:
    if root:
        left_path, right_path = [], []
        if root.left:
            left_path: list = [[root.val] + i for i in SearchAllPath(root=root.left)]
        if root.right:
            right_path: list = [[root.val] + i for i in SearchAllPath(root=root.right)]
        if not root.right and not root.left:
            return [[root.val]]
        return left_path + right_path
    else:
        return []

a = Tree([1,2,3,4,5,None, 6,7])
print(SearchAllPath(a.root_node))
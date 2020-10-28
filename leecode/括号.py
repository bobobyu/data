from mark_time import *


class Solution:
    def __init__(self):
        self.result_list: list = []

    def judge_valid(self, string: str):
        stack_: list = []
        string_index: int = 0
        while string_index < len(string):
            current_op: str = string[string_index]
            if current_op == '(':
                stack_.append(current_op)
                string_index += 1
            elif current_op == ')' and stack_:
                stack_.pop(-1)
                string_index += 1
            else:
                return False
        if not stack_:
            return True
        return False

    def generateParenthesis_(self, n: int, current_string: str = '') -> list:
        if n:
            if current_string != ')' and current_string.count('(') >= current_string.count(')'):
                for op in ['(', ')']:
                    self.generateParenthesis_(n - 1, current_string + op)
        else:
            print(current_string)
            if self.judge_valid(current_string):
                self.result_list.append(current_string)

    @time_
    def generateParenthesis(self, n: int) -> list:
        self.generateParenthesis_(n * 2)
        return self.result_list

    def generate(self, n):
        ans: list = []
        def f(l, r, s):
            l == r == n and ans.append(s)
            l < n and f(l + 1, r, s + '(')
            r < l and f(l, r + 1, s + ')')
        f(0, 0, '')
        return ans


a = Solution()
# a.generateParenthesis(4)
# print(a.result_list)
print(a.generate(3))
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum  =float('-inf')
        def dp(current_node:TreeNode):
            global max_sum
            if current_node:
                left = dp(current_node.left)
                right = dp(current_node.right)
                max_sum = max(max_sum, left + right)
                return max(max_sum, max(left, right) + current_node.val)
            return 0
        return dp(root)
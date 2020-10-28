class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(string: str):
    current_node = ListNode(x=None)
    root = current_node
    while len(string) > 1:
        current_node.val = string[0]
        new_node = ListNode(x=None)
        current_node.next = new_node
        current_node = new_node
        string = string[1:]
    current_node.val = string
    return root


def show_(node: ListNode):
    while node:
        print(node.val, end='')
        node = node.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode(None)
        current_node = result_node
        cf = 0
        while l1 or l2:
            l1val = int(l1.val) if l1 else 0
            l2val = int(l2.val) if l2 else 0
            sum_val = l1val + l2val + cf
            current_node.val = sum_val % 10
            cf = sum_val // 10
            if l1 and l1.next or l2 and l2.next or cf:
                current_node.next = ListNode(None)
                current_node = current_node.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        if cf:
            current_node.val = 1
        return result_node


l1 = create_list('101')
l2 = create_list('99')
a = Solution()
x = a.addTwoNumbers(l1, l2)
show_(x)

class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class CLL:
    def __init__(self,length:int):

        head_node:node = node()
        next_node: node = node()
        tmp_head = head_node
        self.front:node = head_node
        self.rear:node = head_node
        for _ in range(length):
            head_node.next = next_node
            head_node, next_node = next_node, node()
        head_node.next = tmp_head

    def push(self,data):
        if self.rear.next != self.front:
            self.rear = self.rear.next
            self.rear.data = data
            print('入队成功')
        else:print('队伍已满')

    def pop(self):
        if self.rear == self.front:
            print('队伍已空')
        else:
            print('出队成功')
            self.front = self.front.next
    def empty(self):
        return True if self.rear == self.front else False


link:CLL = CLL(5)
for i in range(7):
    link.push(6)
for i in range(6):
    link.pop()
print(link.empty())
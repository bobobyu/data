class LinkNode:
    def __init__(self,data:str=None):
        self.data = data
        self.next = None
        self.prior = None

class Link:
    def __init__(self):
        self.head_node = LinkNode() #头节点

    def CreatLink(self,List:list=None):
        head_point = self.head_node
        for i in range(len(List)):
            next_node = LinkNode(List[i])
            head_point.next = next_node
            next_node.prior = head_point
            head_point = next_node
        head_point.next = self.head_node
        self.head_node.prior = head_point

    def DisPlay_Link(self,head_point:LinkNode):
        if head_point.next != self.head_node:
            print(head_point.next.data)
            self.DisPlay_Link(head_point.next)


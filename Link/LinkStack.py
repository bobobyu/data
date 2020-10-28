from CDLink import *

class LinKStack:
    def __init__(self):
        self.top_Point:LinkNode = LinkNode()
    def Create_Link(self,prior_node:LinkNode = None, data:str = None):
        if len(data)>=1:
            node:LinkNode = LinkNode(data[0])
            if not self.top_Point.data:
                self.top_Point = node
                self.Create_Link(node,data[1:])
            else:
                prior_node.next = node
                self.Create_Link(node, data[1:])
    def Dis_Play_Link(self,Node:LinkNode):
        if Node:
            print(Node.data,end=' ')
            self.Dis_Play_Link(Node.next)
        else:
            print()
    def L_pop(self):
        if self.top_Point:
            tmp:LinkNode = self.top_Point
            self.top_Point = self.top_Point.next
            return tmp
        else:
            return False
    def L_push(self,data:str):
        New_node = LinkNode(data)
        if not self.top_Point:
            self.top_Point = New_node
        else:
            New_node.next = self.top_Point
            self.top_Point = New_node
    def return_top(self):
        return self.top_Point.data
    def Judge_Empty(self):
        if self.top_Point == None:
            return True
        else:
            return False

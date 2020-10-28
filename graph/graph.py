import copy
class graph_node:
    def __init__(self, name:str):
        self.name:str = name
        self.next_node:adj_node = adj_node()
        self.visited:bool = False

class adj_node:
    def __init__(self):
        self.self_node: graph_node = None
        self.next_node: adj_node=  None
        self.value:int = None

    def set_self_node(self, node: graph_node):
        self.self_node= node

    def set_next_node(self, node):
        self.next_node= node

    def set_node_value(self, value:int):
        self.value = value

class graph:

    def __init__(self,data:list):

        "链接字典"

        '''
        将节点存储在字典中，再把节点存储在列表中
        '''

        self.vertices_list = []
        self.vertices_dict: dict = {}

        self.vertices_list = list(set([j for i in data for j in i[0:2]])) #获取所有顶点

        for i in self.vertices_list:
            self.vertices_dict[i] = graph_node(i)  #获取节点对应的字典

        '''
        路径字典
        '''

        self.adj_dic = {} #获取节点的邻接节点字典
        for path in list(set(data)):
            self.adj_dic[path[0]] = self.adj_dic.get(path[0], '') + path[1]

        self.vertices_list = [i for i in list(self.vertices_dict.values())] #获取节点列表

        "邻接矩阵"

        self.Adjacent_Matrix = [[float('inf') for __ in range(len(self.vertices_list)) ] for _ in range(len(self.vertices_list))]
        for path in data:
            self.Adjacent_Matrix[eval(path[0])][eval(path[1])] = path[2]

        self.Distance_Matrix: list = copy.deepcopy(self.Adjacent_Matrix) #距离矩阵
        for i in range(len(self.Adjacent_Matrix)):
            self.Distance_Matrix[i][i] = 0

        '''
        链接表
        '''

        for root, adj_list in self.adj_dic.items():
            prior_node = adj_node()
            self.vertices_dict[root].next_node = prior_node
            prior_node.set_self_node(self.vertices_dict[root])
            for next_one in adj_list:
                next_node = adj_node()
                next_node.set_self_node(self.vertices_dict[next_one])
                prior_node.next_node = next_node
                prior_node.set_node_value(self.Adjacent_Matrix[eval(root)][eval(next_one)])
                prior_node = next_node

    def Deep_First_Search(self, Node: adj_node):
        if Node:
            if not Node.self_node.visited: #如果没有被访问过
                print(Node.self_node.name, end=' ')
                Node.self_node.visited = True
                self.Deep_First_Search(Node.self_node.next_node.next_node) #注意要把下一个地址转到下一个节点去
            else:
                self.Deep_First_Search(Node.next_node) #如果这个节点被访问过，就访问链接表的下一个节点

    def Broad_First_Search(self, node: adj_node):
        if node:
            if not node.self_node.visited:  # 如果没有被访问过
                print(node.self_node.name, end=' ')
                node.self_node.visited = True
                if node.next_node:
                    self.Broad_First_Search(node.next_node) #直接顺着链表向下
                else:
                    self.Broad_First_Search(node.self_node.next_node.next_node) #访问到最后一个节点跳转
            else:
                self.Broad_First_Search(node.next_node)

    # def Dijkstar(self,Start_node: str):
    #     ver_list: list = [[i, j] for i, j in zip(range(len(self.Adjacent_Matrix[eval(Start_node)])), self.Adjacent_Matrix[eval(Start_node)])]
    #     path_length = [[Start_node, 0]]
    #     min_length = float('inf')
    #     for i in ver_list:
    #         if i[-1] < min_length:
    #             min_length = i[-1]
    #             next_node = i
    #     path_length.append(next_node)



a = [ ('0', '1', 5), ('0', '3', 3), ('0', '4', 1), ('1', '0', 4),
      ('1', '2', 1), ('1', '3', 4), ('2', '1', 2), ('2', '3', 9),
      ('2', '4', 5), ('4', '0', 6), ('4', '2', 3), ('4', '3', 7),
      ('3', '1', 3), ('3', '2', 1), ('3', '0', 9), ('3', '4', 7)]

graph_ = graph(a)

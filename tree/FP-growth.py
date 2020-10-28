a = [['f', 'a', 'c', 'd', 'g', 'i', 'm', 'p', ],
     ['a', 'b', 'c', 'f', 'l', 'm', 'o', ],
     ['b', 'f', 'h', 'j', 'o'],
     ['b', 'c', 'k', 's', 'p'],
     ['a', 'f', 'c', 'e', 'l', 'p', 'm', 'n']
     ]


class Node:
    def __init__(self, name: str, value: int):
        self.name: str = name
        self.value: int = value
        self.next_node_list: list = []


class FPGrowth:

    def strip_bracket(self, items):
        if type(items[0]) == type([]) or type(items[0]) == type(()):
            items_ = []
            for i in items:
                items_ += i
            return self.strip_bracket(items_)
        return items

    def padding_item(self, item):
        for i in range(len(self.first_items)):
            if i == len(item):
                item.append(None)
            elif item[i] != self.first_items[i]:
                item.insert(i, None)
        return item

    def __init__(self, items):
        self.first_items_dict: dict = {}
        self.items: list = items
        [self.first_items_dict.update({item: self.first_items_dict.get(item, 0) + 1}) for item in
         self.strip_bracket(items)]
        self.first_items: list = list(self.first_items_dict)
        self.first_items = sorted(self.first_items, key=lambda x: (self.first_items_dict[x], x), reverse=True)
        self.root_node: Node = Node(name='root', value=0)
        self.items.sort(key=lambda x: len(x), reverse=True)
        [self.items[i].sort(key=lambda x: (self.first_items_dict[x], x), reverse=True) for i in range(len(items))]
        self.all_path: list = []

    def gen_tree(self,
                 items: list,
                 current_node: Node,
                 branch_point: bool = False):

        node_name: str = items[0]
        next_name_list: list = [i.name for i in current_node.next_node_list]

        if current_node.name == 'root':

            if node_name in next_name_list:
                index_ = next_name_list.index(node_name)
                self.gen_tree(items=items, current_node=current_node.next_node_list[index_])
            else:
                new_node = Node(name=node_name, value=1)
                current_node.next_node_list.append(new_node)
                self.gen_tree(items=items[1:], current_node=new_node, branch_point=True)

        elif len(items) > 1:
            if not branch_point:
                current_node.value += 1
                if items[1] in next_name_list:
                    index_ = next_name_list.index(items[1])
                    self.gen_tree(items=items[1:], current_node=current_node.next_node_list[index_])
                else:
                    self.gen_tree(items=items[1:], current_node=current_node, branch_point=True)
            else:
                root_name = items[0]
                new_root = Node(name=root_name, value=1)
                current_node.next_node_list.append(new_root)
                self.gen_tree(items=items[1:], current_node=new_root, branch_point=True)
        else:
            if branch_point:
                new_root = items[0]
                current_node.next_node_list.append(Node(name=new_root, value=1))
            else:
                current_node.value += 1

    def generate_absolute_tree(self, items: list):
        self.gen_tree(items=items[0], current_node=self.root_node, branch_point=True)
        for item in items[1:]:
            self.gen_tree(items=item, current_node=self.root_node)

    def generate_path(self, current_node: Node, path: list = []):
        for node in current_node.next_node_list:
            if not node.next_node_list:
                self.all_path.append(path + [{current_node.name: current_node.value}])
            self.generate_path(current_node=node, path=path + [{current_node.name: current_node.value}])

    def generate_tree_and_path(self, items: list):
        self.generate_absolute_tree(items=items)
        self.generate_path(current_node=self.root_node)

    def search_item(self, name: str) -> list:
        result: list = []
        for items in self.all_path:
            temp_list: list = []
            for item in items:
                temp_list.append(item)
                if list(item.keys())[0] == name:
                    result.append(temp_list)
                    break
        return result


x = FPGrowth(a)
x.generate_tree_and_path(a)
print(x.all_path)
print(x.search_item('b'))

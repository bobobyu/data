from typing import List


class StorageBlock:
    def __init__(self, page_index: int = -1):
        self.page_index: int = page_index
        self.next: StorageBlock = None
        self.pre: StorageBlock = None


class PhysicsBlockLink:
    def __init__(self, length: int):
        block_list: List[StorageBlock] = [StorageBlock() for _ in range(length)]
        block_list[0].pre = block_list[-1]
        block_list[-1].next = block_list[0]
        for index, current_block in range(1, len(block_list)):
            pre_block: StorageBlock = block_list[index-1]
            next_block: StorageBlock = block_list[index]
            next_block.pre = pre_block
            pre_block.next = next_block
        self.full_flag: int = length
        self.oldest_block: StorageBlock = block_list[0]
        self.empty_block: StorageBlock = block_list[0]
        self.page_index_view: set = {i.page_index for i in block_list}

    def _call_in_page(self, page_index: int):
        output_list: list = []
        if not self.full_flag:
            if page_index not in self.page_index_view:
                self.empty_block.page_index = page_index
                self.empty_block: StorageBlock = self.empty_block.next
                self.full_flag -= 1
                return 
            else:
                return

class PageReplacementMethod:
    def _load_data(self):
        for index, num in enumerate([int(i) for i in input('Please input page quote string:\n').split(' ')]):
            self.page_quote_string[index] = num
        input('Loading successfully!Press any key to enter algorithm interface:>>>')

    def _initial_algorithm(self):
        self.physics_block_size: int = int(input('Please input the number of physics blocks:'))
        self.page_quote_number: int = int(input('Please input the number of pages quote string:'))
        self.lacking_page_number: int = 0
        self.page_quote_string: List[int] = [-1] * self.page_quote_number
        self.replacement: int = 0
        self.access_hit_rate: float = 0.0


s = PageReplacementMethod()
s._initial_algorithm()
s._load_data()

'''
3
20
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
'''

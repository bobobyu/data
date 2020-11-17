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

        for index, current_block in enumerate(block_list):
            pre_block: StorageBlock = block_list[index - 1]
            next_block: StorageBlock = block_list[index]
            next_block.pre = pre_block
            pre_block.next = next_block

        self.link_size: int = length  # 物理块个数
        self.oldest_block: StorageBlock = block_list[0]  # 指向存在时间最长的物理块
        self.empty_block: StorageBlock = block_list[0]  # 指向一个空的物理块，方便填充
        self.head_block: StorageBlock = block_list[0]  # 指向物理块头块
        self.page_index_view: set = set()  # 存储当前的页面引用号
        self.replacement_count: int = 0  # 置换次数
        self.lacking_page_count: int = 0  # 缺页次数
        self.access_hit_count: int = 0  # 访问命中率
        self.least_recent_dict: dict = {}  # 最近最久访问字典

    def _output_index(self, access_hit: bool) -> list:
        head_block = self.head_block
        if access_hit and (
                len(self.page_index_view) == self.link_size or len(self.least_recent_dict) == self.link_size):
            return [-2] * self.link_size
        result: list = []
        for index in range(self.link_size):
            result.append(head_block.page_index)
            head_block = head_block.next
        return result

    def first_input_first_out(self, *args) -> list:
        access_hit: bool = False
        if args[0] not in self.page_index_view:
            self.lacking_page_count += 1
            if len(self.page_index_view) < self.link_size:
                self.empty_block.page_index = args[0]
                self.empty_block: StorageBlock = self.empty_block.next
                self.page_index_view.add(args[0])
            else:
                self.replacement_count += 1
                new_storage_block: StorageBlock = StorageBlock(page_index=args[0])
                self.page_index_view.discard(self.oldest_block.page_index)
                self.page_index_view.add(args[0])
                if self.oldest_block == self.head_block:
                    self.head_block = new_storage_block
                self.oldest_block.pre.next = new_storage_block
                self.oldest_block.next.pre = new_storage_block
                new_storage_block.next = self.oldest_block.next
                new_storage_block.pre = self.oldest_block.pre
                self.oldest_block = self.oldest_block.next

        else:
            access_hit = True
            self.access_hit_count += 1
        return self._output_index(access_hit=access_hit)

    def optimal_algorithm(self, *args):
        access_hit: bool = False
        if args[0] not in self.page_index_view:
            self.lacking_page_count += 1
            if len(self.page_index_view) < self.link_size:
                self.page_index_view.add(args[0])
                self.empty_block.page_index = args[0]
                self.empty_block = self.empty_block.next

            else:
                self.replacement_count += 1
                string: str = ''
                for i in args[1]:
                    string += str(i)

                replace_page_index: int = max(self.page_index_view,
                                              key=lambda x: string.find(str(x)) if string.find(str(x)) >= 0 else float(
                                                  'inf')
                                              )

                self.page_index_view.discard(replace_page_index)
                self.page_index_view.add(args[0])

                replacement_block: StorageBlock = self.head_block

                while replacement_block.page_index != replace_page_index:
                    replacement_block = replacement_block.next

                new_block: StorageBlock = StorageBlock(page_index=args[0])
                replacement_block.pre.next = new_block
                replacement_block.next.pre = new_block
                new_block.next = replacement_block.next
                new_block.pre = replacement_block.pre

                if replacement_block == self.head_block:
                    self.head_block = new_block

        else:
            access_hit = True
            self.access_hit_count += 1

        return self._output_index(access_hit=access_hit)

    def least_recently_used(self, *args):
        access_hit: bool = False
        for index in self.least_recent_dict:
            self.least_recent_dict[index] += 1
        if args[0] not in self.least_recent_dict:
            self.lacking_page_count += 1
            if len(self.least_recent_dict) < self.link_size:
                self.least_recent_dict[args[0]] = 0
                self.empty_block.page_index = args[0]
                self.empty_block = self.empty_block.next
            else:
                self.replacement_count += 1
                replacement_page_index: int = max(self.least_recent_dict, key=lambda x: self.least_recent_dict[x])
                replacement_block: StorageBlock = self.head_block
                new_block: StorageBlock = StorageBlock(args[0])

                del self.least_recent_dict[replacement_page_index]
                self.least_recent_dict[args[0]] = 0

                while replacement_block.page_index != replacement_page_index:
                    replacement_block = replacement_block.next

                replacement_block.next.pre = new_block
                replacement_block.pre.next = new_block
                new_block.next = replacement_block.next
                new_block.pre = replacement_block.pre

                if replacement_block == self.head_block:
                    self.head_block = new_block
        else:
            access_hit = True
            self.access_hit_count += 1
            self.least_recent_dict[args[0]] = 0

        return self._output_index(access_hit=access_hit)

    def reset_physics_link(self):
        head: StorageBlock = self.head_block
        self.empty_block = self.head_block
        self.oldest_block = self.head_block
        for _ in range(self.link_size):
            head.page_index = -1
            head = head.next
        self.access_hit_count = 0
        self.lacking_page_count = 0
        self.replacement_count = 0
        self.page_index_view.clear()
        self.least_recent_dict.clear()


class PageReplacementMethod:
    def _load_data(self):
        for index, num in enumerate([int(i) for i in input('Please input page quote string:\n').split(' ')]):
            self.page_quote_string[index] = num
        input('Loading successfully!Press any key to enter algorithm interface:>>>')

    def _initial_algorithm(self):
        self.physics_block_size: int = int(input('Please input the number of physics blocks:'))
        self.page_quote_index_number: int = int(input('Please input the number of pages quote string:'))
        self.page_quote_string: List[int] = [-1] * self.page_quote_index_number
        self.physics_block_link: PhysicsBlockLink = PhysicsBlockLink(length=self.physics_block_size)

    def _call_in_page(self, method) -> List[List[int]]:
        _page_quote_string = self.page_quote_string.copy()
        res: List[List] = []
        while _page_quote_string:
            res.append(method(_page_quote_string.pop(0), _page_quote_string))
        return res

    def launch_program(self):
        print('''
        programmer: BoYu-Du
        by:2020/11/17
        summary:This program is used to simulate page replacing function.
        ''')
        self._initial_algorithm()
        self._load_data()
        op_dict: dict = {
            1: self.physics_block_link.first_input_first_out,
            2: self.physics_block_link.optimal_algorithm,
            3: self.physics_block_link.least_recently_used,
        }
        while True:
            print(f'<<<{"-" * 20}>>>')
            print('1:FIFO\t2:OPT\t3:LRU')
            print(f'<<<{"-" * 20}>>>')
            op = int(input('Input the page replace algorithm:'))
            print()
            self._show_outcome(self._call_in_page(op_dict[op]))
            self.physics_block_link.reset_physics_link()

    def _show_outcome(self, result: List[List[int]]):
        [print(i, end='   ') for i in self.page_quote_string]
        print()

        for nums in zip(*result):
            print(' ', end='')
            for index, num in enumerate(nums):
                print(f'|{num}| ' if num >= 0 else f'| | ' if num == -1 else ' ' * 4, end='')
            print()

        print(f'\n\n<<<{"-" * 50}>>>')
        print(
            f'The missing page count: {self.physics_block_link.lacking_page_count}\t\t\t\t\t'
            f'The rate of page missing: {self.physics_block_link.lacking_page_count}/{self.page_quote_index_number}')
        print(
            f'The replacing page number count: {self.physics_block_link.replacement_count}\t\t\t'
            f'The rate of access hit: '
            f'{(self.physics_block_link.access_hit_count / self.page_quote_index_number) * 100:.2f}%')
        print(f'<<<{"-" * 50}>>>\n\n')


s = PageReplacementMethod()
s.launch_program()

from typing import List


class StorageNode:
    def __init__(self, start_address: int = None, length: int = None):
        self.start_address: int = start_address
        self.length: int = length
        self.state = True
        self.next: StorageNode = None
        self.pre: StorageNode = None

    def _allocation_storage(self, allocation_length: int):
        if allocation_length <= self.length:
            self.length -= allocation_length
            self.state = False if not self.length else True
            self.start_address += allocation_length
            if not self.state:
                self.pre.next = self.next
                if self.next:
                    self.next.pre = self.pre



class ContinueStorageAllocationManagement:
    def __init__(self, file_name: str):
        self.storage_list: list = []
        self.work_dict: dict = {}
        with open(file_name) as f:
            for i in f.readlines():
                current_storage_list: list = [int(i) for i in i.split(' ')]
                if not self.storage_list:
                    head_node: StorageNode = StorageNode(start_address=current_storage_list[0],
                                                              length=current_storage_list[1])
                    previous_node: StorageNode = head_node
                    self.storage_list.append(previous_node)
                else:
                    current_node: StorageNode = StorageNode(start_address=current_storage_list[0],
                                                            length=current_storage_list[1])
                    previous_node.next = current_node
                    self.storage_list.append(current_node)
                    current_node.pre = previous_node
                    previous_node = current_node
        self.empty_node: StorageNode = StorageNode()
        head_node.pre = self.empty_node
        self.empty_node.next = head_node
        # [print(i.start_address,i.length, end=' ') for i in self.storage_list]

    def continue_storage_allocation_management(self):
        allocation_function: dict = {
            1: self._first_fit_allocation_storage_space,
            2: self._best_fit_allocation_storage_space,
            3: self._worst_fit_allocation_storage_space,
            4: self._take_back_work

        }

        while True:
            self._show_free_storages_information()
            choice: int = int(input('1:first-fit\n2:best-fit\n3:worst-fit\n4:take-back\n0:exit\n:'))
            if choice == 0:
                return
            if not allocation_function.get(choice):
                print('!!!Input error!!!')
            allocation_function[choice]()


    def _show_free_storages_information(self):
        print(f'<{"-" * 20}\tCurrent Free Table\t\t{"-" * 20}>')
        print('Start-Address\tLength\tState')
        head: StorageNode = self.empty_node
        while head:
            if head.length:
                print(f'{head.start_address}\t\t\t\t{head.length}\t\t{head.state}')
            head = head.next
        print(f'\n<{"-" * 20}\tCurrent Free Table\t\t{"-" * 20}>\n\n')

        print(f'<{"-" * 20}\tCurrent Allocated Table\t{"-" * 20}>')
        print('Start-Address\tLength\tWork-Name')
        for name, inf in self.work_dict.items():
            print(f'{inf["start_address"]}\t\t\t\t{inf["length"]}\t\t{name}')
        print(f'\n<{"-" * 20}\tCurrent Allocated Table\t{"-" * 20}>')

    def _first_fit_allocation_storage_space(self) -> None:
        work_name, work_size = input('Please input work name and size of space:').split(' ')
        work_size = int(work_size)

        def search_available_storage_address(work_size, head_=self.empty_node.next) -> list:
            if head_.length >= work_size:
                head_._allocation_storage(allocation_length=work_size)
                return [True, head_, head_.start_address - work_size]
            elif head_.next:
                return search_available_storage_address(work_size=work_size, head_=head_.next)
            else:
                return [False, None, None]

        flag, storage, start_address = search_available_storage_address(work_size=work_size)
        if not flag:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')
            return
        else:
            self.work_dict[work_name] = {'storage_address': storage,
                                         'start_address': start_address,
                                         'length': work_size}

    def _best_fit_allocation_storage_space(self) -> None:
        sorted_list: List[StorageNode] = sorted(self.storage_list, key=lambda x: x.length)
        work_name, work_size = input('Please input work name and size of space:').split(' ')
        work_size = int(work_size)

        def search_available_storage_address(work_size: int) -> list:
            for storage in sorted_list:
                if storage.length >= work_size:
                    storage._allocation_storage(work_size)
                    return [True, storage, storage.start_address - work_size]
            return [False, None, None]

        flag, storage, start_address = search_available_storage_address(work_size)
        if flag:
            self.work_dict[work_name] = {'storage_address': storage,
                                         'start_address': start_address,
                                         'length': work_size}
        else:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')

    def _worst_fit_allocation_storage_space(self) -> None:
        sorted_list: List[StorageNode] = sorted(self.storage_list, key=lambda x: x.length, reverse=True)
        work_name, work_size = input('Please input work name and size of space:').split(' ')
        work_size = int(work_size)

        def search_available_storage_address(work_size: int) -> list:
            for storage in sorted_list:
                if storage.length >= work_size:
                    storage._allocation_storage(work_size)
                    return [True, storage, storage.start_address - work_size]
            return [False, None, None]

        flag, storage, start_address = search_available_storage_address(work_size)
        if flag:
            self.work_dict[work_name] = {'storage_address': storage,
                                         'start_address': start_address,
                                         'length': work_size}
        else:
            print('!!!!Current don\'t have enough storage space to allocate.Please try again!!!!')

    def _take_back_work(self):
        work_name: str = input('Please input witch work name you want to take back:')
        work_inf: dict = self.work_dict[work_name]
        if work_inf:
            storage_: StorageNode = work_inf['storage_address']
            length: int = work_inf['length']
            storage_.start_address -= length
            storage_.length += length
            storage_.state = True
            head = self.empty_node
            for storage in self.storage_list:
                head.next = storage
                storage.pre = head
                head = storage
            del self.work_dict[work_name]
        else:
            print('Work name not exist!Please try again!')


s = ContinueStorageAllocationManagement('C:\\Users\\n\\Desktop\\TestFile.txt')
s.continue_storage_allocation_management()

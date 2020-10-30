import random


class Progress:
    def __str__(self):
        return f'{self.ID}\t\t\t' \
               f'{self.ArriveTime}\t\t\t\t\t' \
               f'{self.CPUTime}\t\t\t\t' \
               f'{self.AllTime}\t\t\t\t' \
               f'{self.Priority}\t\t' \
               f'{self.State}'

    def __init__(self, ID: int = -1, Priority: int = None):
        self.ID = ID
        self.Priority: int = random.randint(0, 10) if not Priority else Priority
        self.AllTime: int = random.randint(0, 200)
        self.State: int = ProgressControlScheduling.READY
        self.ArriveTime: int = 0
        self.CPUTime: int = 0
        self.Counter: int = 0
        self.next: Progress = None


class ProgressControlScheduling:
    READY: int = 0
    RUNNING: int = 1
    BLOCK: int = 3
    OVER: int = 4

    def __init__(self, num_of_progress: int) -> None:
        pre_PCB: Progress = Progress(ID=1)
        self.PCB_length: int = num_of_progress
        self.count_PCB: int = num_of_progress
        self.head_PCB: Progress = pre_PCB
        self.PCB_list: list = [pre_PCB]
        for i in range(2, num_of_progress + 1):
            next_PCB: Progress = Progress(ID=i)
            self.PCB_list.append(next_PCB)
            pre_PCB.next = next_PCB
            pre_PCB = next_PCB

    def LaunchProgressControlScheduling(self):
        algorithm: dict = {
            1: self._FCFS,
            2: self._SJF,
            3: self._PS,
            4: self._RR,
        }
        name_list: list = ['FCFS', 'SJF', 'PS', 'RR']
        print('Condition of Progress:')
        print(len(self.PCB_list))
        self._Display(self.head_PCB)
        while True:
            print('Alternative Algorithm:')
            [print(f'Press {i + 1} : {j}') for i, j in enumerate(name_list)]
            num = eval(input('Your option(Enter -1 to exit):'))
            if num == -1:
                break
            algorithm.get(num, '')()

    def _Display(self, head: Progress, current_PCB: Progress = None, name: str = '', time: int = 0):
        print(f'{time} time.Current PCB ID:{head.ID if not current_PCB else current_PCB.ID}' if time <= len(
            self.PCB_list) else f'Finish {name}.Show queue:')
        print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
        if time > self.PCB_length and name not in ['PSA', 'SJF']:
            head = self.head_PCB
        while head:
            if head.Priority >= 0:
                print(head)
            head = head.next
        print()

    def conclusion(self, total_waiting_time: int):
        print(f'The average time of each progress：{total_waiting_time / self.PCB_length}s.')
        print(f'Total time of all progress：{total_waiting_time}s.')

    def _sort_PCB(self, key: str) -> list:
        if key == 'AllTime':
            return sorted(self.PCB_list, key=lambda x: x.AllTime)
        else:
            return sorted(self.PCB_list, key=lambda x: x.Priority, reverse=True)

    def reset(self, queue_list: list) -> Progress:
        for progress_index in range(len(queue_list) - 1):
            queue_list[progress_index].next = queue_list[progress_index + 1]
        queue_list[-1].next = None
        head: Progress = queue_list[0]
        yield head
        for progress_index in range(len(queue_list) - 1):
            queue_list[progress_index].CPUTime, queue_list[progress_index].AllTime = queue_list[
                                                                                         progress_index].AllTime, \
                                                                                     queue_list[
                                                                                         progress_index].CPUTime
            queue_list[progress_index].State = ProgressControlScheduling.READY
            queue_list[progress_index].ArriveTime = 0
        queue_list[-1].CPUTime, queue_list[-1].AllTime = queue_list[-1].AllTime, queue_list[-1].CPUTime
        queue_list[-1].State = ProgressControlScheduling.READY
        queue_list[-1].ArriveTime = 0

    def search_special_PCB(self, head: Progress, type: str = 'P') -> Progress:
        pre_PCB: Progress = head
        current_PCB: Progress = head.next

        pre_alternative_PCB: Progress = pre_PCB
        alternative_PCB: Progress = current_PCB

        compare_dict: dict = {'P': lambda x, y: x.Priority < y.Priority, 'T': lambda x, y: x.AllTime > y.AllTime}

        while current_PCB:
            if compare_dict[type](alternative_PCB, current_PCB):
                alternative_PCB = current_PCB
                pre_alternative_PCB = pre_PCB
            pre_PCB = current_PCB
            current_PCB = current_PCB.next
        pre_alternative_PCB.next = alternative_PCB.next
        alternative_PCB.next = None
        return alternative_PCB

    def add_head(self) -> Progress:
        head_: Progress = Progress(Priority=-1)
        head_.next = self.PCB_list[0]
        return head_

    def _FCFS(self):
        print(f'\n{"-" * 35}Launch FCFS{"-" * 35}\n')
        each_waiting_time: int = 0
        total_waiting_time: int = 0
        current_node: Progress = self.PCB_list[0]
        count_time: int = 1
        while current_node:
            current_node.State = ProgressControlScheduling.RUNNING
            each_waiting_time += current_node.AllTime
            total_waiting_time += each_waiting_time
            current_node.CPUTime = current_node.AllTime
            current_node.AllTime = 0
            self._Display(current_node, name="FCFS", time=count_time)
            count_time += 1
            current_node.State = ProgressControlScheduling.OVER
            current_node = current_node.next
        self._Display(current_node, name="FCFS", time=count_time)
        self.conclusion(total_waiting_time=total_waiting_time)
        print(f'\n{"-" * 35} Finish FCFS {"-" * 35}\n')
        [_ for _ in self.reset(self.PCB_list)]

    def _SJF(self):
        print(f'\n{"-" * 35} Launch SJF {"-" * 35}\n')
        queue_list: list = []
        each_waiting_time: int = 0
        total_waiting_time: int = 0
        count_: int = self.PCB_length
        head: Progress = self.add_head()
        while count_:
            current_node = self.search_special_PCB(head=head, type='T')
            queue_list.append(current_node)
            current_node.State = ProgressControlScheduling.RUNNING
            each_waiting_time += current_node.AllTime
            total_waiting_time += each_waiting_time
            current_node.AllTime, current_node.CPUTime = 0, current_node.AllTime
            self._Display(head=head, current_PCB=current_node, name='SJF', time=self.PCB_length - count_ + 1)
            current_node.State = ProgressControlScheduling.OVER
            count_ -= 1
        head = next(self.reset(queue_list=queue_list))
        self._Display(head=head, name='SJF', time=self.PCB_length + 1)
        self.conclusion(total_waiting_time=total_waiting_time)
        print(f'{"-" * 35} Finish SJF {"-" * 35}\n')
        [_ for _ in self.reset(self.PCB_list)]

    def _PS(self):
        print(f'\n{"-" * 35} Launch 优先调度算法 {"-" * 35}\n')
        queue_list: list = []
        head_root: Progress = self.add_head()
        count_ = self.PCB_length
        each_waiting_time: int = 0
        total_waiting_time: int = 0
        while count_:
            current_PCB: Progress = self.search_special_PCB(head=head_root, type='P')
            current_PCB.State = ProgressControlScheduling.RUNNING
            each_waiting_time += current_PCB.AllTime
            total_waiting_time += each_waiting_time
            current_PCB.CPUTime, current_PCB.AllTime = current_PCB.AllTime, 0
            self._Display(head=head_root, name='PSA', time=self.PCB_length - count_ + 1, current_PCB=current_PCB)
            count_ -= 1
            queue_list.append(current_PCB)
            current_PCB.State = ProgressControlScheduling.OVER
        head_PCB = next(self.reset(queue_list=queue_list))
        self._Display(head=head_PCB, name='PSA', time=len(queue_list) + 1)
        self.conclusion(total_waiting_time=total_waiting_time)
        print(f'{"-" * 35}Finish 优先调度算法{"-" * 35}\n')
        [_ for _ in self.reset(self.PCB_list)]

    def _RR(self):
        time_slice = int(input('Please input the size of time slice:'))
        next_PCB: Progress = self.head_PCB
        count_PCB: int = self.count_PCB
        all_time_list: list = [i.AllTime for i in self.PCB_list]
        pre_root: Progress = Progress()
        pre_root.next = next_PCB
        end_root: Progress = Progress()
        self.PCB_list[-1].next = end_root
        end_root.next = pre_root
        each_waiting_time: int = 0
        total_waiting_time: int = 0

        while count_PCB:
            if next_PCB.ID > 0:
                next_PCB.AllTime = max(0, next_PCB.AllTime - time_slice)
                next_PCB.CPUTime = min(next_PCB.CPUTime + time_slice, all_time_list[next_PCB.ID - 1])
                each_waiting_time += time_slice if next_PCB.AllTime >= time_slice else time_slice - next_PCB.AllTime
                total_waiting_time += each_waiting_time
                print(f'PCB:{next_PCB.ID}\tAllTime:{next_PCB.AllTime}\tCPUTime:{next_PCB.CPUTime}')
                if not next_PCB.AllTime:
                    print(f'PCB:{next_PCB.ID} having finished.')
                    next_PCB = next_PCB.next
                    pre_root.next = next_PCB
                    count_PCB -= 1
                    continue
            pre_root = next_PCB
            next_PCB = next_PCB.next
        print(f'The average time of each progress：{total_waiting_time / len(all_time_list)}s.')
        print(f'Total time of all progress：{total_waiting_time}s.')
        print(f'{"-" * 35}Finish 优先调度算法{"-" * 35}\n')
        [_ for _ in self.reset(self.PCB_list)]


test = ProgressControlScheduling(5)
test.LaunchProgressControlScheduling()

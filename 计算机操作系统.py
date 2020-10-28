import random
import time


class Progress:
    def __str__(self):
        return f'{self.ID}\t\t\t' \
               f'{self.ArriveTime}\t\t\t\t\t' \
               f'{self.CPUTime}\t\t\t\t' \
               f'{self.AllTime}\t\t\t\t' \
               f'{self.Priority}\t\t' \
               f'{self.State}'

    def __init__(self, ID: int = -1):
        self.ID = ID
        self.Priority: int = random.randint(0, 10)
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
        self._Display(self.head_PCB)
        while True:
            print('Alternative Algorithm:')
            [print(f'Press {i + 1} : {j}') for i, j in enumerate(name_list)]
            num = eval(input('Your option(Enter -1 to exit):'))
            if num == -1:
                break
            algorithm.get(num, '')()

    def _Display(self, head: Progress, name: str = '', time: int = 0):
        print(f'{time} time.Current PCB ID:{head.ID}' if time <= len(
            self.PCB_list) else f'Finish {name}.Show queue:')
        print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
        if time > len(self.PCB_list):
            head = self.head_PCB
        while head:
            print(head)
            head = head.next
        print()

    def conclusion(self, total_waiting_time: int):
        print(f'The average time of each progress：{total_waiting_time / len(self.PCB_list)}s.')
        print(f'Total time of all progress：{total_waiting_time}s.')

    def _sort_PCB(self, key: str) -> list:
        if key == 'AllTime':
            return sorted(self.PCB_list, key=lambda x: x.AllTime)
        else:
            return sorted(self.PCB_list, key=lambda x: x.Priority, reverse=True)

    def reset(self):
        for progress_index in range(len(self.PCB_list) - 1):
            self.PCB_list[progress_index].CPUTime, self.PCB_list[progress_index].AllTime = self.PCB_list[
                                                                                               progress_index].AllTime, \
                                                                                           self.PCB_list[
                                                                                               progress_index].CPUTime
            self.PCB_list[progress_index].State = ProgressControlScheduling.READY
            self.PCB_list[progress_index].ArriveTime = 0
            self.PCB_list[progress_index].next = self.PCB_list[progress_index + 1]
        self.PCB_list[-1].CPUTime, self.PCB_list[-1].AllTime = self.PCB_list[-1].AllTime, self.PCB_list[-1].CPUTime
        self.PCB_list[-1].State = ProgressControlScheduling.READY
        self.PCB_list[-1].ArriveTime = 0
        self.PCB_list[-1].next = None

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
        self.reset()

    def _SJF(self):
        print(f'\n{"-" * 35}Launch SJF{"-" * 35}\n')
        queue_list: list = self.PCB_list[:]
        service_queue: list = self._sort_PCB(key='AllTime')
        each_waiting_time: int = 0
        total_waiting_time: int = 0
        for time, progress in enumerate(service_queue):
            progress.State = ProgressControlScheduling.RUNNING
            progress.ArriveTime = each_waiting_time
            each_waiting_time += progress.AllTime
            total_waiting_time += each_waiting_time
            progress.CPUTime = progress.AllTime
            progress.AllTime = 0
            progress.State = ProgressControlScheduling.OVER
            queue_list.remove(progress)
            print(f'Search minimum running time PCB:{progress.ID}')
            print(f'{time + 1} times executed algorithm. Show ready queue: ')
            print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
            [print(i) for i in queue_list]
        print(f'The finish queue:')
        print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
        [print(i) for i in service_queue]
        print(f'The average time of each progress：{total_waiting_time / len(service_queue)}s.')
        print(f'Total time of all progress：{total_waiting_time}s.')
        print(f'{"-" * 35}Finish SJF{"-" * 35}\n')
        self.reset()

    def _PS(self):
        print(f'\n{"-" * 35}Launch 优先调度算法{"-" * 35}\n')
        queue_list: list = self.PCB_list[:]
        service_queue: list = self._sort_PCB(key='Priority')
        each_waiting_time: int = 0
        total_waiting_time: int = 0
        for time, progress in enumerate(service_queue):
            progress.State = ProgressControlScheduling.RUNNING
            progress.ArriveTime = each_waiting_time
            each_waiting_time += progress.AllTime
            total_waiting_time += each_waiting_time
            progress.CPUTime = progress.AllTime
            progress.AllTime = 0
            progress.State = ProgressControlScheduling.OVER
            queue_list.remove(progress)
            print(f'Search minimum running time PCB:{progress.ID}')
            print(f'{time + 1} times executed algorithm. Show ready queue: ')
            print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
            [print(i) for i in queue_list]
        print(f'The finish queue:')
        print(f'ID\t\tArriveTime\t\tCPUTime<Occupied>\t\tAllTime\t\tPriority\tState')
        [print(i) for i in service_queue]
        print(f'The average time of each progress：{total_waiting_time / len(service_queue)}s.')
        print(f'Total time of all progress：{total_waiting_time}s.')
        print(f'{"-" * 35}Finish 优先调度算法{"-" * 35}\n')
        self.reset()

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
        self.reset()


test = ProgressControlScheduling(5)
test.LaunchProgressControlScheduling()

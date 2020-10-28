from SqStack import *
from Squeue import *

class Ccar:
    def __init__(self, ID:int, time:int):
        self.ID: int = ID
        self.timestamp:int = time

    def exit_cmp_time(self, time:int):
        interval_time:int = time - self.timestamp
        return interval_time


class Cpark:

    def __init__(self, n:int):
        self.Stall:SqStack = SqStack()
        self.Entrance:Squeue = Squeue()
        self.Max_Capacity:int = n
        self.parking_fee_rate = 0.01

    def enter(self,enter_time:int, ID:int):
        park_flag:bool = False
        car_inf:Ccar = Ccar(ID=ID, time=enter_time)
        self.Entrance.push(data=car_inf)
        if self.Stall.length() < self.Max_Capacity: #如果停车栈未满，则将队列的第一辆车停入栈中
            self.Stall.S_push(self.Entrance.pop())
            park_flag = True
        print(f"牌照：{car_inf.ID},停车时间：{enter_time}, 停车状态：{'成功' if park_flag else '等待'}")

    def exit(self,ID:int, exit_time:int):
        tmp_stack:SqStack = SqStack()

        while self.Stall.return_top().ID != ID:
            tmp_stack.S_push(self.Stall.S_pop())

        '''
        指定车辆出栈，计算停车费
        '''

        exit_car:Ccar = self.Stall.S_pop()
        interval_time:int = exit_car.exit_cmp_time(exit_time)
        print(f"牌照：{exit_car.ID}，停车费用：{interval_time*self.parking_fee_rate}")

        '''
        出栈的车顺序返回
        '''

        while not tmp_stack.judege_empty():
            self.Stall.S_push(tmp_stack.S_pop())

        '''
        队首车入栈
        '''
        front_car:Ccar = self.Entrance.pop()
        front_car.exit_cmp_time(exit_time)  # 假设上一个车的出栈时间就是队首车入栈时间
        print(f"牌照：{front_car.ID}, 停车时间：{exit_time}, 停车状态：成功")
        self.Stall.S_push(front_car)

    def display_Stall_inf(self):
        print()
        print(f'>>>{"-"*10}输入停车场信息{"-"*10}<<<')
        for i in self.Stall.Stack:
            print(f"|\t\t牌照：{i.ID},停入时间：{i.timestamp}\t\t\t|")
        print(f'>>>{"-" * 31}<<<')
        print()



park:Cpark = Cpark(3)
park.enter(0, 1000)
park.enter(1, 1001)
park.enter(2, 1002)
park.enter(3, 1003)
park.display_Stall_inf()
park.exit(ID=1000, exit_time=4)
park.display_Stall_inf()


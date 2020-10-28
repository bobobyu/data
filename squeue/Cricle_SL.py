class CSL:
    def __init__(self,Capacity:int):
        self.rear:int = 0
        self.front:int = 0
        self.Max_Capacity:int = Capacity
        self.list_: list = [None for _ in range(Capacity)]
    def pop(self):
        if self.rear == self.front:
            print('队伍已空')
        else:
            self.front += 1
            self.front %= self.Max_Capacity
    def push(self, data):
        if (self.rear + 1) % self.Max_Capacity  == self.front:
            print('队伍已满')
        else:
            self.rear += 1
            self.rear %= self.Max_Capacity
            self.list_[self.rear] = data
    def empty(self):
        return True if self.rear == self.front else False

    def display(self):
        index:int = self.rear
        while index != self.front:
            print(self.list_[index])
            index  = self.Max_Capacity - 1 if index - 1 < 0 else index -1


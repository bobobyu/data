class Squeue:
    def __init__(self):
        self.squeue:list = []
    def push(self,data:str):
        self.squeue.append(data)
    def judge_empty(self):
        return True if not len(self.squeue) else False
    def pop(self):
        return self.squeue.pop(0) if not self.judge_empty() else False
    def lenghth(self):
        return len(self.squeue)

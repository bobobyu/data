class SqStack:
    def __init__(self):
        self.Stack:list = []
    def S_pop(self):
        if not self.Stack:
            return False
        return self.Stack.pop(-1)
    def S_push(self,data:str):
        self.Stack.append(data)
    def return_top(self):
        return self.Stack[-1]
    def length(self):
        return len(self.Stack)
    def judege_empty(self):
        return True if not len(self.Stack) else False
    def pop_special_elem(self,feature):
        pass
    def display(self):
        [print(i,end=' ') for i in self.Stack]
        print()

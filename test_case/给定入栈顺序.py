from SqStack import *
# sqlist : list = [eval(i) for i in input().split(' ')]
test = [3, 4, 1, 2]

Stack_1 = SqStack()
Stack_2 = SqStack()

[Stack_1.S_push(str(i)) for i in test]
length:int = Stack_1.length()
while not Stack_1.judege_empty():
    print(f'<{"-" * 15}>')
    print("初始栈：",end='->')
    Stack_1.display()
    print("辅助栈：", end='->')
    Stack_2.display()
    print(f'<{"-"*15}>\n')

    if Stack_2.judege_empty() or Stack_2.return_top() < Stack_1.return_top():
        Stack_2.S_push(Stack_1.S_pop())
    elif Stack_1.return_top() < Stack_2.return_top():
        tmp_2:str = Stack_2.S_pop()
        tmp_1:str = Stack_1.S_pop()
        Stack_1.S_push(tmp_2)
        Stack_2.S_push(tmp_1)
while not Stack_2.judege_empty():
    Stack_1.S_push(Stack_2.S_pop())
Stack_1.display()
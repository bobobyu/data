from SqStack import *

prior_dic: dict = {"+": 0, "-": 0, "*": 1, "/": 1, "(": -1}
op_list: list = [i for i in prior_dic.keys()]
op_stack: SqStack = SqStack()
no_stack: SqStack = SqStack()
string: str = "(5*(1+3))/2"

for op_nmb in string:
    # print(op_nmb)
    # print(op_stack.Stack)
    # print(no_stack.Stack)
    # print()
    if op_nmb in op_list:
        if op_nmb == "(":
            op_stack.S_push(op_nmb)
        else:
            while not op_stack.judege_empty() and prior_dic[op_nmb] < prior_dic[op_stack.return_top()]:
                if op_stack.return_top() != "(":
                    no_stack.S_push(op_stack.S_pop())
                else:
                    op_stack.S_pop()
            op_stack.S_push(op_nmb)
    elif op_nmb == ")":
        while op_stack.return_top() != '(':
            no_stack.S_push(op_stack.S_pop())
        op_stack.S_pop()
    else:
        no_stack.S_push(op_nmb)

while not op_stack.judege_empty(): #把运算符栈的所有元素出栈
    no_stack.S_push(op_stack.S_pop())

Postfix_expression: list = []
while not no_stack.judege_empty():
    Postfix_expression.insert(0, no_stack.S_pop())
print(Postfix_expression)

op_dic = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}

import time
def compute_value(Pos_list: list):
    i: int = 0
    while len(Postfix_expression) > 1:
        print(Pos_list)
        time.sleep(0.01)
        if Pos_list[i] not in op_list and Pos_list[i + 1] not in op_list and Pos_list[i + 2] in op_list:
            print(Pos_list[i],Pos_list[i+1])
            values: float = op_dic[Pos_list[i + 2]](float(Pos_list[i]), float(Pos_list[i + 1]))
            Pos_list.insert(i, values)
            [Pos_list.pop(i+1) for _ in range(3)]
        i += 1
        i %= len(Pos_list) - 2
    print(Pos_list)

compute_value(Postfix_expression)
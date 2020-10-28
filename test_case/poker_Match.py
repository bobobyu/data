a: list = [i for i in '241256']
b: list = [i for i in '313564']

stack:list = []
op: bool = True

while a and b:
    print(stack)
    print(f"{a}<-" if op else a)
    print(f"{b}<-" if not(op) else b)
    if op:
        stack.append(a.pop(0))
        tmp:str = stack[-1]
        if stack.count(stack[-1]) > 1:
            a.append(stack.pop(-1))
            while stack[-1] != tmp:
                a.append(stack.pop(-1))
            a.append(stack.pop(-1))
    else:
        stack.append(b.pop(0))
        tmp: str = stack[-1]
        if stack.count(stack[-1]) > 1:
            b.append(stack.pop(-1))
            while stack[-1] !=tmp:
                b.append(stack.pop(-1))
            b.append(stack.pop(-1))
    op = not(op)
    print()
print('templatetags' if not(b) else 'b')






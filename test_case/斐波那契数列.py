# def Fibonacci(n:int, current_num:int=1, rear_num:int=0):
#     if n == 1:
#         return current_num
#     else:
#         return Fibonacci(n - 1, current_num + rear_num, current_num)

def FIB(n:int):
    a:int = 0
    b:int = 1
    for i in range(n):
        a,b = b,a+b
        yield b


for i in FIB(5):
    print(i)

    '''
    1 1 2 3 5 8
    '''
a = 1
b = 0

for i in range(10):
    a, b = b, a
    b = a+b
    print(b)
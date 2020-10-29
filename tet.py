def x(n):
    for i in range(10):
        print(i)
        yield
next(x(1))
print()
[_ for _ in x(2)]
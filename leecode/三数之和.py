re = []
def product_itertools(items: list, time: int, self: bool = True, result: list = []) -> None:
    if time:
        for i in items:
            if self:
                product_itertools(items=items, time=time - 1, result=result + [i])
            else:
                items_copy = items[:]
                items_copy.remove(i)
                product_itertools(items=items_copy, time=time - 1, result=result + [i], self=False)
    else:
        re.append(result)


# def product_itertools_(items: list, time: int, self: bool = True) -> list:
#     if time:
#         for i in items:
#             if self:
#                 return [i] + [product_itertools(items=items, time=time - 1)]
#             else:
#                 items_copy = items[:]
#                 items_copy.remove(i)
#                 product_itertools(items=items_copy, time=time - 1, self=False)
#     else:
#         return []


product_itertools(items=[1, 3, 2, 4], time=4, self=False)
print(re)

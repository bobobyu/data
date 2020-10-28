
def flatten(list_):
    if type(list_) in [type([]), type(()), type({})]:
        for i in list_:
            if type(i) in [type([]), type(()), type({})]:
                return flatten(i[0])
            else:
                return [i]
    else:
        return [list_]

a = [[[1]],[2]]
print(flatten(a))
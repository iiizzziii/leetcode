def zzz(lst : int or str, fact : int):
    new_lst = []
    for l in lst:
        new_lst.append(l*fact)
    print(new_lst)

zzz([3,4,5,6], 2)
zzz(["a","b","c"], 3)
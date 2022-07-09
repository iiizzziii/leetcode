def zzz(lst: int or str, rem_ele: int or str):
    if not lst:
        print("empty list")
    elif rem_ele not in lst:
        print("not found")
    else:
        new_lst = []
        for l in lst:
            if l != rem_ele:
                new_lst.append(l)
        print(new_lst)

zzz([1,2,3,4], 2)
zzz([3,3,2,1], 3)
zzz(["a","b","c","b"], "b")
zzz([3,4,5,6], 7)
zzz([], 0)
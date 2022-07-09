def zzz(lst: int or str, rm_el: int or str):
    if not lst:
        print("empty list")
    elif rm_el not in lst:
        print("not found")
    else:
        new_lst = []
        for l in lst:
            if l != rm_el:
                new_lst.append(l)
        print(new_lst)

zzz([1,2,3,4], 2)
zzz([3,3,2,1], 3)
zzz(["a","b","c","b"], "b")
zzz([3,4,5,6], 7)
zzz([], 0)
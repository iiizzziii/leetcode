def zzz(lst: int or str):
    lst = list(dict.fromkeys(lst))
    print(lst)

zzz([1,1,2,3,4,4])
zzz(["a","a","b","a"])
zzz([1,2,3])
zzz([])
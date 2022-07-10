def zzz(lst:int):
    if len(lst) < 2:
        print("none")
    else:
        lst.remove(max(lst))
        print(max(lst))

zzz([1,2,3,4])
zzz([1,2])
zzz([2])
zzz([])
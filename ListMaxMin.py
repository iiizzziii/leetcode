def zzz(lst : int):
    if not lst:
        print(None)
    else:
        print(str(max(lst)), str(min(lst)))

zzz([3,4,5,6])
zzz([-1,-2,-3,-4])
zzz([0,0,0,0])
zzz([])
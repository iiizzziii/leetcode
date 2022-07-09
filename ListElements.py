def zzz(lst : int or str):
    if not lst:
        print("empty list")
    else:
        for l,elem in enumerate(lst):
            print(elem, l)

zzz([1,2,3,4])
zzz(["a","b","c"])
zzz([])
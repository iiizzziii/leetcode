def zzz(lst1:int,lst2:int):
    if not lst1:
        print(lst1)
    lst = []
    for e in lst1:
        if e not in lst2:
            lst.append(e)
    print(lst)

zzz([1,2,3,4],[1,2])
zzz([1,2,3,4],[1,2,3])
zzz([1,2,3,4],[1,2,3,4])
zzz([],[1,3])
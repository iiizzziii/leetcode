def zzz(lst:int or str):
    lst2set = set(lst)
    set2dict = dict.fromkeys(lst2set)
    for l in lst2set:
        counter = lst.count(l)
        set2dict[l] = counter
    print(set2dict)

zzz(["a","a","b","c","a","b"])
zzz([1,2,3,4,3,2,1,2])
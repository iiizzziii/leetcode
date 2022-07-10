def zzz(lst:int or str):
    big_lst = []
    for l in lst:
        if not isinstance(l, list):
            big_lst.append(l)
        else:
            for i in l:
                big_lst.append(i)
    set(big_lst)
    print(big_lst)

zzz([[1,2,3],[4,5,6],[7,8,9]])
zzz([1,2,3,4,5,6,[7,8,9]])
zzz([["a","b","c"],["d","e","f"],["g","h","i"]])
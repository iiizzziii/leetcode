from itertools import permutations

def zzz(lst:int):
    perm = permutations(lst)
    for l in list(perm):
        print(l)

zzz([1,2,3])
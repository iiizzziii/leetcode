def zzz(lst:int):
    counter = 0
    for l in lst:
        if l > 3:
            counter+=1
    print(counter)

zzz([1,-1,0,2,2,3])
zzz([1,2,3,4])
zzz([7,8,9,10])
zzz([])
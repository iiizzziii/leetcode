import math

def zzz(pa:int,pb:int):
    dis = (((pb[0]-pa[0])**2) + ((pb[1]-pb[1])**2) + ((pb[2]-pb[2])**2))
    final = math.sqrt(dis)
    print(final)

zzz([1,2,3],[1,2,3])
zzz([3,4,5],[1,3,5])
zzz([-3,4,-5],[2,0,-4])
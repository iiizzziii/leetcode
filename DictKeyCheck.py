def zzz(dic:int or str,key:int or str):
    # if key in dic:
    #     print("True")
    # else:
    #     print("False")
    print(key in dic)

zzz({"a":4,"b":6}, "a")
zzz({"a":4,"b":6}, "c")
zzz({}, "d")
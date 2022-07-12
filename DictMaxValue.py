def zzz(dic:int or str):
    if not dic:
        print("none")
    else:
        print(max(dic.values()))

zzz({"a":4,"b":3,"c":7})
zzz({"a":4,"b":6})
zzz({"a":4,"b":4})
zzz({})
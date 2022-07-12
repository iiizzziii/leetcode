def zzz(dic: int or str):
    checker = len(set(dic.values()))
    if not checker:
        print("empty")
    elif checker == 1:
        print("values are the same")
    else:
        print("values are not the same")

zzz({"a":4,"b":4,"c":4})
zzz({"a":4,"b":6,"c":4})
zzz({"a":4,"b":6,"c":10})
zzz({})
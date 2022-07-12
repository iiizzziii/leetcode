def zzz(new_key:int or str,new_value:int):
    ini_dic = {"January":45,"February":56,"March":67}

    if new_key not in ini_dic.keys():
        ini_dic[new_key] = new_value
        print(ini_dic)
    else:
        print("key already exists")
        print(f"{new_key} {new_value}")

zzz("April",67)
zzz("January",67)
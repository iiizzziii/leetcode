from heapq import merge


def zzz(my_dict1,my_dict2:str or int):
    final_dict = my_dict1|my_dict2
    print(final_dict)

zzz({"a": 1, "b": 2, "c": 3},{"c": 4, "d": 6, "e": 8})
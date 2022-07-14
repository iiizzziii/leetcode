from sqlalchemy import values


def zzz(dic:int or str):
    dic2set = set(dic.values())
    values2list = list(dic.values())
    new_dic = {}

    for x in dic2set:
        counts = values2list.count(x)
        new_dic[x] = counts

    print(new_dic)

zzz({
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 })
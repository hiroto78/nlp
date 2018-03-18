import re

data = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. '
        'New Nations Might Also Sign Peace Security Clause. Arthur King Can.')
data_ary = list(map(lambda x: re.sub('[,.]', '', x), data.split(' ')))
target_ary = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ret = {}

for index, item in enumerate(data_ary):
    if index + 1 in target_ary:
        ret[item[:1]] = index
    else:
        ret[item[:2]] = index
print(ret)

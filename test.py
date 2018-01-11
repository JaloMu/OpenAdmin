# -*- coding: utf-8 -*-
# @Time    : 2017/11/7 下午5:24
# @Author  : Jalo.Mu
# @Site    : 
# @File    : test.py.py
# @Software: PyCharm

import yaml

from ServiceModule.cmdb.types import encode

with open('meta.yaml') as f:
    p = yaml.load(f)


print(p)
# for k, v in p.items():
#     c = encode(k, v)
#     print(c)
#     y = decode(k, c)
#     print(type(y))
for k, v in p['type'].items():
    c = encode(k, **v)
    print(c)


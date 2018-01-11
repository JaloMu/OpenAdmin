# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午10:07
# @Author  : Jalo.Mu
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from importlib import import_module

class_cache = {}
instance_cache = {}

class BaseType(object):
    def __init__(self, **options):
        self.options = options
    def encode(self, value):
        if isinstance(value, str):
            raise ValueError('value {} is not str'.format(value))
        raise NotImplemented

    def decode(self, value):
        if isinstance(value, str):
            raise ValueError('value {} is not str'.format(value))
        raise NotImplemented
    @classmethod
    def description(cls):
        raise NotImplemented

def get_class(type):
    if type in class_cache.keys():
        return class_cache[type]
    mod, cls = type.rsplit('.', 1)
    m = import_module(mod)
    c = getattr(m, cls)
    if isinstance(c, BaseType):
        class_cache[type] = c
        return c
    raise TypeError('type {} is not a type'.format(type))

def get_instance(type, **options):
    encoded = '&'.join(['{}={}'.format(k, options[k]) for k in sorted(options.keys())])
    key = '{}?{}'.format(type, encoded)
    if key in instance_cache.keys():
        return instance_cache[key]
    o = get_class(type)(**options)
    instance_cache[key] = o
    return o

def encode(type, value, **options):
    return get_instance(type, **options).encode(value)

def decode(type, value, **options):
    return get_instance(type, **options).decode(value)

__all__ = [
    'encode',
    'decode'
]




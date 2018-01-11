# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午10:09
# @Author  : Jalo.Mu
# @Site    : 
# @File    : cmdbtype.py
# @Software: PyCharm

from ServiceModule.cmdb.types import BaseType
import re
from ipaddress import ip_address

class IPVersion(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class IPValue(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class String(BaseType):
    def encode(self, value):
        return value
    def decode(self, value):
        return value

class Int(BaseType):
    '''
        @encode value -> str
        @decode value -> str
    '''
    def encode(self, value):
        val = int(value)
        if 'max' in self.options.keys() and val > int(self.options['max']):
            raise ValueError('value {} too bigger'.format(val))
        if 'min' in self.options.keys() and val < int(self.options['min']):
            print(val ,self.options['min'])
            raise ValueError('value {} too small'.format(val))
        return value

    def decode(self, value):
        return value

    @classmethod
    def description(cls):
        return ''''
        # Int
        ## options:
        
        * max:
        * min: 
        '''

class IPV4(BaseType):
    def encode(self, value):
        if (len(value.split('.')) != 4):
            raise ValueError
        return str(int(ip_address(value.decode())))

    def decode(self, value):
        return str(ip_address(int(value)))

class IPV6(BaseType):
    def _validate_ip(self, value):
        _HEX_RE = re.compile(r'^:{0,1}([0-9a-fA-F]{0,4}:){0,7}[0-9a-fA-F]{0,4}:{0,1}$')
        _DOTTED_QUAD_RE = re.compile(r'^:{0,1}([0-9a-fA-F]{0,4}:){2,6}(\d{1,3}\.){3}\d{1,3}$')
        if _HEX_RE.match(value):
            if ':::' in value:
                return False
            if '::' not in value:
                halves = value.split(':')
                return len(halves) == 8 and halves[0] != '' and halves[-1] != ''
            halves = value.split('::')
            if len(halves) != 2:
                return False
            if halves[0] != '' and halves[0][0] == ':':
                return False
            if halves[-1] != '' and halves[-1][-1] == ':':
                return False
            return True

        if _DOTTED_QUAD_RE.match(value):
            if ':::' in value:
                return False
            if '::' not in value:
                halves = value.split(':')
                return len(halves) == 7 and halves[0] != ''
            halves = value.split('::')
            if len(halves) > 2:
                return False
            hextets = value.split(':')
            quads = hextets[-1].split('.')
            for q in quads:
                if int(q) > 255 or int(q) < 0:
                    return False
            return True
        return False
    def encode(self, value):
        if (self._validate_ip(value)):
            return str(int(ip_address(value.decode())))
        raise IPValue('value error %s' % value)


    def decode(self, value):
        return str(ip_address(int(value)))
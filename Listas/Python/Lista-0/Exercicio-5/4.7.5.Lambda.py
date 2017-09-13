# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print f(0)
print f(1)
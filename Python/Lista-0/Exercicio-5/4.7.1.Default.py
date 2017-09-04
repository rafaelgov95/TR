# -*- coding: utf-8 -*-
print "Exemplo 1"
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while 1:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'): return True
        if ok in ('n', 'no', 'nop', 'nope'): return False
        retries = retries - 1
        if retries < 0: raise IOError, 'refusenik user'
        print complaint

print ask_ok('Do you really want to quit?')
print ask_ok('OK to overwrite the file?', 2)


print "\nExemplo 2"

i = 5
def f(arg = i):
    print arg
i = 6
f()

print "\nExemplo 3"

def f(a, L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)

print "\nExemplo 4"
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

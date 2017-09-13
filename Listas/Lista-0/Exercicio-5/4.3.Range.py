# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

print "Exemplo 1"
a=range(10)
print a
print "\nExemplo 2 "
a=range(5, 10)
print a
a=range(0, 10, 3)
print a
a=range(-10, -100, -30)
print a
print "\nExemplo 3 "
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]
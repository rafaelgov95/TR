# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

print "Exemplo 1"
print (1, 2, 3)              < (1, 2, 4)
print [1, 2, 3]              < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)           < (1, 2, 4)
print (1, 2)                 < (1, 2, -1)
print(1, 2, 3)             == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'Lista.pyab'))   < (1, 2, ('abc', 'a'), 4)
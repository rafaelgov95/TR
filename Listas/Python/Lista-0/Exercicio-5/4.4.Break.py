# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

for n in range(2, 10): #cria uma sequencia de numeros de 2 a 10.
    for x in range(2, n):
          if n % x == 0:
              print n, 'equals', x, '*', n/x
              break
    else:
              print n, 'is a prime number'
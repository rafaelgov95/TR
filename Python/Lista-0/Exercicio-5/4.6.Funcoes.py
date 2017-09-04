# -*- coding: utf-8 -*-
print "Exemplo 1"
def fib(n):
    """Print a Fibonacci series up to n"""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

fib(2000)
print "\n\nExemplo 2"
print fib
print "\nExemplo 3"
print fib(0)
print "\nExemplo 4"

def fib2(n):
      # Retorna a lista contendo a serie de Fibonacci ate n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)  # veja abaixo
        a, b = b, a + b
    return result

f100 = fib2(100)    # invoca
print f100          # escreve resultado
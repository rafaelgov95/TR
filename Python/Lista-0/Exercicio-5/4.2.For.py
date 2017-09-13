# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

print "Exemplo 1"
a = ['gato', 'janela', 'defenestrar']
for x in a:
    print x, len(x)
print "\nExemplo 2"
for x in a[:]: # faz uma cópia da lista inteira
    if len(x) > 6: a.insert(0, x)

print a
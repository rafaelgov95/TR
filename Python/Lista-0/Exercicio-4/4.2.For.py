# Medindo algumas strings:
# -*- coding: utf-8 -*-
print "Exemplo 1"
a = ['gato', 'janela', 'defenestrar']
for x in a:
    print x, len(x)
print "\nExemplo 2"
for x in a[:]: # faz uma cópia da lista inteira
    if len(x) > 6: a.insert(0, x)

print a
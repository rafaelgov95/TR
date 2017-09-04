# -*- coding: utf-8 -*-

print "Exemplo 1"
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
print "Camada 1"
parrot(1000)
print "Camada 2"
parrot(action = 'VOOOOOM', voltage = 1000000)
print "Camada 3"
parrot('a thousand', state = 'pushing up the daisies')
print "Camada 4"
parrot('a million', 'bereft of life', 'jump')

print "\nExemplo 2"
print (" Modo invalido")
# parrot()                     # parâmetro exigido faltando
# parrot(voltage=5.0, 'dead')  # parâmetro não-chave-valor depois de parâmetro chave-valor
# parrot(110, voltage=220)     # valor duplicado para mesmo parâmetro
# parrot(actor='John Cleese')  # parâmetro desconhecido")
print "\nExemplo 3"

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, '?'
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments: print arg
    print '-'*40
    keys = keywords.keys()
    keys.sort()
    for kw in keys: print kw, ':', keywords[kw]

cheeseshop('Limburger', "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               client='John Cleese',
               shopkeeper='Michael Palin',
               sketch='Cheese Shop Sketch')
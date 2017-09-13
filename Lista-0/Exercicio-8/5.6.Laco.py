# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

print "Exemplo 1"
knights = {'Angular': 'Bom', 'Ruby': 'O Fácil'}
for k, v in knights.iteritems():
    print k, v

print "\nExemplo 2"

for i, v in enumerate(['Ola', 'Mundo', 'Novo']):
    print i, v

print "\nExemplo 3"
questions = ['Codigo', 'Linguagem', 'Cor Markting']
answers = ['JavaScript', 'Angular', 'Vermelho']
for q, a in zip(questions, answers):
    print ' %s?  %s.' % (q, a)

print "\nExemplo 4"
for i in reversed(xrange(1,10,2)):
    print i

print "\nExemplo 5"
basket = ['Coding', 'Black', 'Mundo', 'Novo', 'Oque isso', 'Fui Fui']
for f in sorted(set(basket)):
    print f
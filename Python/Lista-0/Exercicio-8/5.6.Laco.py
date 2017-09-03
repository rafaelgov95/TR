# -*- coding: UTF-8 -*-

print "Exemplo 1"
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

print "\nExemplo 2"

for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

print "\nExemplo 3"
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your %s?  It is %s.' % (q, a)

print "\nExemplo 4"
for i in reversed(xrange(1,10,2)):
    print i

print "\nExemplo 5"
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f
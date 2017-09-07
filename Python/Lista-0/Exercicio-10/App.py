# -*- coding: utf-8 -*-

from Modelo.Arvore import Arvore

if __name__ == '__main__':
    arvore = Arvore('S')
    arvore.add('R')
    arvore.add('A')
    arvore.add('F')
    arvore.add('A')
    arvore.add('E')
    arvore.add('L')
    arvore.add('*')
    arvore.add('V')
    arvore.add('I')
    arvore.add('A')
    arvore.add('N')
    arvore.add('A')
    print "IN - ORDEM"
    arvore.inordem()
    print "PRE - ORDEM"
    arvore.preordem()
    print "POS -ORDEM"
    arvore.posordem()
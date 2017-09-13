# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

from Modelo.Arvore import Arvore

if __name__ == '__main__':
    arvore = Arvore('S')
    arvore.inserir('R')
    arvore.inserir('A')
    arvore.inserir('F')
    arvore.inserir('A')
    arvore.inserir('E')
    arvore.inserir('L')
    arvore.inserir('*')
    arvore.inserir('V')
    arvore.inserir('I')
    arvore.inserir('A')
    arvore.inserir('N')
    arvore.inserir('A')
    print "IN - ORDEM"
    arvore.inordem()
    print "PRE - ORDEM"
    arvore.preordem()
    print "POS -ORDEM"
    arvore.posordem()
# -*- coding: utf-8 -*-

from Modelo.Node import Node

if __name__ == '__main__':
    tree = Node('S')
    tree.add('E')
    tree.add('X')
    tree.add('A')
    tree.add('R')
    tree.add('C')
    tree.add('H')
    tree.add('M')
    print "IN - ORDEM"
    tree.inordem()
    print "PRE - ORDEM"
    tree.preordem()
    print "POS -ORDEM"
    tree.posordem()
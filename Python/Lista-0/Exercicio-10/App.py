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
    tree.percorre("pos")
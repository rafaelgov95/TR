# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

from Node import Node
class Arvore (object):

    def __init__(self,root=None):
        self.root = Node(root);

    preordem = lambda self: self.root.preordem()
    posordem =lambda self: self.root.posordem()
    inordem = lambda self: self.root.inordem()
    buscar = lambda self,key: self.root.buscar(key)
    inserir = lambda self,key: self.root.inserir(key)
    remove = lambda self,key:self.root.remove(key)

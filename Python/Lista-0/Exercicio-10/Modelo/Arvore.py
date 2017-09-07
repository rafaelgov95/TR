# -*- coding: UTF-8 -*-
from Node import Node
class Arvore (object):

    def __init__(self,root=None):
        self.root = Node(root);

    preordem = lambda self: self.root.preordem()
    posordem =lambda self: self.root.posordem()
    inordem = lambda self: self.root.inordem()
    get = lambda self,key: self.root.get(key)
    add = lambda self,key: self.root.add(key)
    remove = lambda self,key:self.root.remove(key)

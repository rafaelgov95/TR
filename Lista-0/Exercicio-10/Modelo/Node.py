# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

class Node(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def posordem(self):
        if self.left:
            self.left.posordem()
        if self.right:
            self.right.preordem()
        print self.key

    def inordem(self):
        if self.left:
            self.left.inordem()
        print self.key
        if self.right:
            self.right.inordem()

    def preordem(self):
        print self.key
        if self.left:
           self.left.preordem()
        if self.right:
           self.right.preordem()

    def buscar(self, chave):
        if self.key == chave:
            return self
        node = self.left if chave < self.key else self.right
        if node is not None:
            return node.buscar(chave)

    def inserir(self, key):
        metade = 'left' if key < self.key else 'right'
        node = getattr(self, metade)
        if node is None:
            setattr(self, metade, Node(key))
        else:
            node.inserir(key)

    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            t = self.right._min()
            self.key, self.value = t.key, t.value
            self.right._deleteMin()
        return self

    def _min(self):
        if self.left is None:
            return self
        else:
            return self.left._min()

    def _deleteMin(self):
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._deleteMin()
        return self


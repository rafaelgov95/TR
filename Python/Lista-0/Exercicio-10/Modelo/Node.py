# -*- coding: UTF-8 -*-

class Node:

    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right
        self.conta = 1


    def get(self, key):
        if key > self.key:
            if not self.right is None:
                return self.right.get(key)
            else:
                return None
        elif key < self.key:
            if not self.left is None:
                return self.left.get(key)
            else:
                return None
        else:
            return self.key

    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            # ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self.right._min()
            self.key = tmp.key
            self.right._remove_min()
            return self

    def _min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:
            return self
        else:
            return self.left._min()

    def _remove_min(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._removeMin()
        return self

    def add(self, key):
        if self.get(key) is None:
            if key > self.key:
                self.addright(key)
            elif key < self.key:
                self.addleft(key)
            else:
                self.conta = self.conta + 1
        else:
            print "Erro ao Adicionar " + str(key) + " já foi adicionado."

    def addleft(self, valor):
        if self.left:
            self.left.add(valor)
        else:
            self.left = Node(valor)

    def addright(self, valor):
        if self.right:
            self.right.add(valor)
        else:
            self.right = Node(valor)

    def preordem(self):
        if not self is None:
            print self.key
            if self.left:
                 self.preordem()
            if self.right:
                 self.preordem()

    def inordem(self,node=None):
        if not self is None:
            if self.left:
                self.left.inordem()
            print self.key
            if self.right:
                self.right.inordem()

    def posordem(self):
        if not self is None:
            if self.left:
                self.posordem()
            if self.right:
                self.preordem()
        print self.key
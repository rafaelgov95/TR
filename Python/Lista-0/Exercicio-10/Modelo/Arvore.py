# -*- coding: UTF-8 -*-

class Arvore (object):
    
    def __init__(self, key, value=None, left=None, right=None):

        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):

        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self

    def add(self, node):

        if self.get(node.key) is None:
          if node.value < self.value:
              if self.left is None:
                  self.left = node
              else:
                  self.left.add(node)
          else:
              if self.right is None:
                  self.right = node
              else:
                  self.right.add(node)
        else:
            print "O Numero ",node.key," já foi adicionado !!"
            return

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
            self.key, self.value = tmp.key, tmp.value
            self.right._remove_min()
        return self.key

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

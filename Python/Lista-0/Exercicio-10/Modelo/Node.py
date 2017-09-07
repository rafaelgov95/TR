# -*- encoding:utf-8 -*-
from __future__ import print_function


class Node(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    def add(self, key):
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, Node(key))
        else:
            node.add(key)

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

    def traverse(self, visit, order='pre'):

        if order == 'pre':
            visit(self.key)
        if self.left is not None:
            self.left.traverse(visit, order)
        if order == 'in':
            visit(self.key)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'pos':
            visit(self.key)

    def percorre(self, order='pre'):
        self.traverse(print, order)

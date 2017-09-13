# -*- coding: UTF-8 -*-
# Autor: Rafael Viana


class No(object):

   def __init__(self,valor=None,proximo=None,pai=None):
       self.valor = valor
       self.proximo = proximo
       self.pai=pai

   getValor = lambda self: self.valor
   getProximo = lambda self: self.proximo
   getPai = lambda self: self.pai

   def setValor(self, valor):
       self.valor = valor

   def setProximo(self, proximo):
       self.proximo = proximo

   def setPai(self, pai):
       self.pai = pai
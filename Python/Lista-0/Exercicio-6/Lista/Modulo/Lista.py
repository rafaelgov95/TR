# -*- coding: UTF-8

from No import No

class Lista(object):

   def __init__(self,valor=None):
        self.root = No(valor) if valor else None

   def inserirNoFim(self, valor):
       if self.root:
           temp = self.root
           while(temp.getProximo()):
               temp = temp.getProximo()
           temp.setProximo(No(valor))
       else:
           self.root = No(valor)

   def insereInicio(self, valor):
      if self.root:
          temporario = No(valor)
          temporario.setProximo(self.root)
          self.root = temporario
      else:
          self.root = No(valor)

   def percorreListaEncadeada(self):
      temp = self.root
      while(temp):
          if temp.getValor:
              print temp.getValor()
              temp = temp.getProximo()

   def removeInicio(self):
      temporario = self.getProximo()
      self.setProximo(temporario.getProximo())
      return temporario.getValor()


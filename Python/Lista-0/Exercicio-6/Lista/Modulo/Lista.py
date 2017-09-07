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

   def inserir(self, valor,index=None):
       if self.root:
           if(index==0):
               self.insereInicio(valor)
           else:
               temp = self.root
               cont = 0
               while(temp.getProximo() and cont<index-1):
                   cont+=1
                   temp = temp.getProximo()
               if(temp.getProximo()):
                    tempo = No(valor)
                    tempo.setProximo(temp.getProximo())
                    temp.setProximo(tempo)
               else:
                   temp.setProximo(No(valor))
       else:
           self.root = No(valor)

   def percorreListaEncadeada(self):
      temp = self.root
      while(temp):
          if temp.getValor:
              print temp.getValor()
              temp = temp.getProximo()

   def remover(self,valor=None):
        if(valor):
            if (valor == self.root.getValor()):
                self.root = No()
            else:
                temp = self.root
                while(temp.getProximo().getValor()!=valor):
                    temp = temp.getProximo()
                tempo = temp.getProximo().getProximo()
                temp.setProximo(tempo)


        else:
            temp = self.root.getProximo()
            valor = self.root.getValor()
            self.root = temp
            return valor


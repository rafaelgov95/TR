# -*- coding: UTF-8

class Lista:

   def __init__(self,valor=None):
       self.valor = None
       self.proximo = None

   getValor = lambda self : self.valor
   getProximo = lambda self : self.proximo

   def setValor(self, valor):
      self.valor = valor

   def setProximo(self, proximo):
      self.proximo = proximo


   def insereInicio(self, valor):
      if self:
          temporario = Lista()
          temporario.setProximo(self.getProximo())
          temporario.setValor(valor)
          self.setProximo(temporario)
      else:
          self=Lista()

   def percorreListaEncadeada(self):
      temp = self
      while(temp):
          if temp.getValor:
              print"aqui", temp.getValor()
              temp = temp.getProximo()

   def removeInicio(self):
      temporario = self.getProximo()
      self.setProximo(temporario.getProximo())
      return temporario.getValor()


if __name__ == "__main__":
    # testes da classe Lista
    f = Lista("Angular2")
    f.insereInicio("Angular")
    f.insereInicio("C++")
    # f.insereInicio("Java")
    # f.insereInicio("JavaScript")
    # f.insereInicio("Python")
    f.percorreListaEncadeada()
    # f.removeInicio()
    # print "\nUm valor foi removido Removido \n"
    # f.percorreListaEncadeada()

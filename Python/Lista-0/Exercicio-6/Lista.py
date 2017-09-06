
def main():
    # testes da classe Fila
    f = Lista()
    f.insereInicio("Angular")
    f.insereInicio("C++")
    f.insereInicio("Java")
    f.insereInicio("JavaScript")
    f.insereInicio("Python")
    f.percorreListaEncadeada()
    f.removeInicio()
    print "\nUm valor foi removido Removido \n"
    f.percorreListaEncadeada()


class Lista:

   def __init__(self,valor=None):
       self.valor = None
       self.proximo = None

   getValor = lambda self : self.valor
   getProximo = lambda self : self.proximo

   def setValorOrbital(self, valor):
      self.valor = valor

   def setProximo(self, proximo):
      self.proximo = proximo


   def insereInicio(self, valor):
      if self.valor:
          temporario = Lista()
          temporario.setProximo(self.getProximo())
          temporario.setValorOrbital(valor)
          self.setProximo(temporario)
      self.valor=valor

   def percorreListaEncadeada(self):
      while(self != None):
         print self.getValor()
         self = self.getProximo()


   def removeInicio(self):
      temporario = self.getProximo()
      self.setProximo(temporario.getProximo())
      return temporario.getValor()



main()
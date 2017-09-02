# -*- coding: UTF-8 -*-

def main():

    f = Lista()
    f.inserir("Angular",0)
    f.inserir("C++",1)
    f.inserir("Java",1)
    f.inserir("JavaScript",5)
    f.inserir("Python",0)
    f.inserirFim("NodeJs")

    print f.getAll()
    f.remover("Python")
    f.remover("NodeJs")
    f.remover("JavaScript")
    print f.get("C++")
    print f.getIndex("C++")
    print f.getAll()

class Lista(object):

    def __init__(self):
        self.elementos = []

    inserirFim =  (lambda self, elemento: self.elementos.insert(len(self.elementos),elemento))

    def inserir(self,elemento,index=None):
        if index is None:
            self.elementos.append(elemento)
        else:
            self.elementos.insert(index, elemento)

    vazia = lambda self: len(self.elementos) == 0

    def get(self,elemento):
        if not self.vazia():
            try:
                result = self.elementos[self.elementos.index(elemento)]
                return result
            except ValueError:
                return("Valor Não Existe")
        else:
            return ("Lista Vazia")

    def getAll(self):
        if not self.vazia():
                return self.elementos
        else:
            return ("Lista Vazia")

    def getIndex(self,elemento):
        if not self.vazia():
            try:
                result =self.elementos.index(elemento)
                return result
            except ValueError:
                return("Valor Não Existe")
        else:
            return ("Lista Vazia")

    def remover(self,elemento):
        if not self.vazia():
            return self.elementos.remove(elemento)


main()
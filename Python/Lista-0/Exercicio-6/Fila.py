# -*- coding: UTF-8 -*-

def main():
    # testes da classe Fila
    f = Fila(10)
    f.inserir("Angular")
    f.inserir("C++")
    f.inserir("Java")
    f.inserir("JavaScript")
    f.inserir("Python")
    print f.elementos
    print(f.remover())
    print(f.remover())
    print(f.remover())
    print(f.remover())

class Fila:
    def __init__(self, max):
        self.elementos = [0]*max # cria uma fila com max elementos, todos zero
        self.ini = 0
        self.fim  = 0
    def inserir(self, ele):
        self.elementos[self.fim] = ele
        self.fim += 1
    def remover(self):
        obj = self.elementos[self.ini]
        self.ini += 1
        return obj

main()
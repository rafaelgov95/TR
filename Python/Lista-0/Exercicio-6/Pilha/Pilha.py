# -*- coding: UTF-8 -*-

class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

if __name__ == "__main__":
# teste da class Pilha
    f = Pilha()
    f.empilha("Angular")
    f.empilha("C++")
    f.empilha("Java")
    f.empilha("JavaScript")
    f.empilha("Python")
    print(f.desempilha())
    print(f.desempilha())
    print(f.desempilha())
    print(f.desempilha())
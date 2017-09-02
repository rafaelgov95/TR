# -*- coding: UTF-8 -*-

def main():

    f = Pilha()
    f.inserir("Angular")
    f.inserir("C++")
    f.inserir("Java")
    f.inserir("JavaScript")
    f.inserir("Python")
    print(f.desempilha())
    print(f.desempilha())
    print(f.desempilha())
    print(f.desempilha())


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

main()
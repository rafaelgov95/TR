# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

from Modulo.Pilha import Pilha


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
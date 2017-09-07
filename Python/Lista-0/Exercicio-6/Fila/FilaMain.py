# -*- coding: UTF-8 -*-
from Modulo.Fila import Fila


if __name__ == "__main__":
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
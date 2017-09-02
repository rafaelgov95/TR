# -*- coding: UTF-8 -*-

from Modelo.Arvore import Arvore

def main():
    root = Arvore(0)
    root.add(Arvore(2))
    root.add(Arvore(2))
    root.remove(2)


def pt ():
    pass

if __name__ == "__main__": # Chamada Principal da Aplicação.
    main()
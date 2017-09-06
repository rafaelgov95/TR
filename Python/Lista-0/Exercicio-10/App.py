# -*- coding: utf-8 -*-

from Modelo.Arvore import Arvore

def main():
    root = Arvore("A")
    # root.add("B")
    # root.add("C")
    # root.add("D")
    # root.add("E")
    # root.add("F")
    # root.add("G")
    # root.add("H")
    # root.add("I")
    print "Removeu : "+ str(root.remove("A").key)
    # root.preordem()
    # root.posordem()

    root.inordem()

if __name__ == "__main__": # Chamada Principal da Aplicação.
    main()
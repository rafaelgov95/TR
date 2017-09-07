# -*- coding: UTF-8
from Modulo.Lista import Lista

if __name__ == "__main__":
    # testes da classe Lista
    f = Lista()
    f.insereInicio("Angular")
    f.insereInicio("C++")
    f.inserirNoFim("Python")
    f.insereInicio("Rafael O Rei")
    f.inserir("Rafael",10)
    f.percorreListaEncadeada()
# -*- coding: UTF-8
from Modulo.Lista import Lista

if __name__ == "__main__":
    # testes da classe Lista
    f = Lista() # cria uma Lista
    print "Exemplo 1"
    f.insereInicio("Angular")# Adiciona no Inicio
    f.inserirNoFim("Python")# Adiciona no Fim

    f.insereInicio("C++")# Adiciona no Inicio
    f.inserir("Rafael",3)# Adiciona em qualquer possição da Lista
    f.remover("Rafael")  # Percorre a lista e remove o primeiro 'Angular'
    f.insereInicio("Angular")  # Adiciona no Inicio
    f.inserirNoFim("Python")  # Adiciona no Fim

    f.insereInicio("C++")  # Adiciona no Inicio
    f.inserir("Rafael", 3)  # Adiciona em qualquer possição da Lista
    f.percorreListaEncadeada()


    print "\nExemplo 2" # Limpar Lista

    f.clean()  # Limpar Lista

    f.percorreListaEncadeada()

    print "\nExemplo 3"

    f.insereInicio("Angular")  # Adiciona no Inicio
    f.inserirNoFim("Python")  # Adiciona no Fim

    f.insereInicio("C++")  # Adiciona no Inicio
    f.inserir("Rafael", 3)  # Adiciona em qualquer possição da Lista
    f.remover("Angular")# Percorre a lista e remove o primeiro 'Angular'

    print f.get("C++")
    # Percorre a lista e busca o primeiro 'Rafael'

    f.percorreListaEncadeada()
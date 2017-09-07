# -*- coding: UTF-8
from Modulo.Lista import Lista

if __name__ == "__main__":
    # testes da classe Lista
    f = Lista() # cria uma Lista
    f.insereInicio("Angular")# Adiciona no Inicio
    f.inserirNoFim("Python")# Adiciona no Fim
    f.insereInicio("Rafael O Rei")# Adiciona no Inicio
    f.inserir("Rafael",3)# Adiciona em qualquer possição da Lista
    f.remover("Angular")# Percorre a lista e remove o primeiro 'Angular'
    f.get("Rafael")# Percorre a lista e busca o primeiro 'Rafael'
    f.clean()# Limpar Lista
    f.percorreListaEncadeada()
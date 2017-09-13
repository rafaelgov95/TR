# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

from Arquivo import Arquivo
from Quick import Quick

if __name__ == "__main__":
     lista = Arquivo.AcessarArquivo() # Faz a leitura do Documento Numeros
     start = 0 # Inicio do Quick
     end = len(lista) - 1 # Fim Do Quick
     Quick.quicksort(lista, start, end) # Realizando a ordenação pelo QuickSorte
     #Mapeando para uma melhor visualização
     print ' '.join(map(str, lista))



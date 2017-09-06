# -*- coding: UTF-8 -*-
import Arquivo
import Quick

if __name__ == "__main__":
     lista = Arquivo.AcessarArquivo()
     # lista = [2,3,4,56,2,1,0]
     start = 0
     end = len(lista) - 1
     Quick.quicksort(lista, start, end)
     print lista
     #Mapeando para uma melhor visualização
     print ' '.join(map(str, lista))



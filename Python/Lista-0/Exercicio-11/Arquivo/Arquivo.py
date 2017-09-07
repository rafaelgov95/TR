# -*- coding: UTF-8 -*-

def AcessarArquivo():
    arquivo = open('Numeros', 'r') # abre o documento Numeros
    NewList= '' # Cria uma variavel string vazia, para armazenar os numeros extraidos do documento
    for line in arquivo: # for
         NewList+=(line.strip()) # metodo strip() serve para tirar o \n
    arquivo.close() # Fecha conexão
    r = map(int,NewList.split(';')) # map realiza a conversão em int e split faz o parse dos numeros entregando em uma lista
    return r
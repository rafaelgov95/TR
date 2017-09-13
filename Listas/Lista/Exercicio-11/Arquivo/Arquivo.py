# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

def AcessarArquivo():
    arquivo = open('Numeros', 'r') # abre o documento Numeros
    NewList= '' # Cria uma variavel string vazia, para armazenar os numeros extraidos do documento
    r =[]
    for line in arquivo: # for
         NewList+=(line.strip()) # metodo strip() serve para tirar o \n
         r = map(int, NewList.split(';'))  # map realiza a conversão em int e split faz o parse dos numeros entregando em uma lista
    arquivo.close() # Fecha conexão
    return r
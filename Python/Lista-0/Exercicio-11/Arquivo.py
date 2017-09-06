# -*- coding: UTF-8 -*-

def AcessarArquivo():
    arquivo = open('Numeros', 'r')
    NewList= ''
    for line in arquivo:
         NewList+=(line.strip())
    arquivo.close()
    r = map(int,NewList.split(';'))
    return r
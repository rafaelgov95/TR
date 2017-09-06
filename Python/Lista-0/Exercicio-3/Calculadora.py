# -*- coding: UTF-8 -*-
#Autor: Rafael Viana
def main():
    while(1):
        menuInicial()
        print "Resultado: "+ str(sevira(input('Digite um das operações acima !\n')))

def lerNumero():
    valor1 = input('Digite primeiro valor !\n')
    valor2 = input('Digite segundo valor !\n')
    return valor2 ,valor1

def sevira (operacao,):
    lista = lerNumero()
    if(operacao==1):
        return lista[1] + lista[0]
    elif (operacao == 2):
        return lista[1] - lista[0]
    elif (operacao == 3):
        return lista[1] / lista[0]
    elif (operacao == 4):
        return lista[1] * lista[0]


def menuInicial():
    print "Bem Vindo a Mega Calculadora em Python\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n"


main()


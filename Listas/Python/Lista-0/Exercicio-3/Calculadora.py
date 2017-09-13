# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

def main():
    while(1):
        print menuInicial()
        print "\nResultado: "+ str(sevira(input('Digite um das operações acima !\n')))+"\n"


menuInicial = lambda: "Bem Vindo a Mega Calculadora em Python\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n"

def lerNumeros():
    valor1 = input('Digite primeiro valor !\n')
    valor2 = input('Digite segundo valor !\n')
    return valor2 ,valor1

def sevira (operacao,):
    lista = lerNumeros()
    if(operacao==1):
        return float(lista[1]) + float(lista[0])
    elif (operacao == 2):
        return float(lista[1]) - float(lista[0])
    elif (operacao == 3):
        return float(lista[1]) / float(lista[0])
    elif (operacao == 4):
        return float(lista[1]) * float(lista[0])

main()


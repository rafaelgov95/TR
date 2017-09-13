# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

import ModulosPythons.Servicos

# Exemplo -9

# Objetivo: Esse exemplo tem como objetivo demostrar a
# utilização de um modulo.
# Foi criado um Pacote de serviços diversos que
# contém Funções como Data Atual, Preço do Bitcoin atual ,
# Preço do Real Atual e Preço do Dolar Atual atraves de APIs da internet.

#Hora Atual
print  ModulosPythons.Servicos.agora() # Esse aqui e um teste
# Valor do bitcoin em uma funcao no modulo :D
print "Valor do Bitcoin R$:'%.4f' " % ModulosPythons.Servicos.bitcoin()
print ModulosPythons.Servicos.Valores()
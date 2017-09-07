# -*- coding: UTF-8 -*-

import ModulosPythons.Servicos

# Exemplo -9

# Objetivo: Esse exemplo tem como objetivo demostrar a criação de um modulo. Foi criado um modulo de serviços diversos que
# contém Funções como Data Atual, Preço do Bitcoin atual , Preço do Real Atual e Preço do Dolar Atual atraves da internet.


print  ModulosPythons.Servicos.agora() # Esse aqui e um teste
print "Valor do Bitcoin R$:'%.4f' " % ModulosPythons.Servicos.bitcoin()# Valor do bitcoin em uma funcao no modulo :D
print ModulosPythons.Servicos.Valores()
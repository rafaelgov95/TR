# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

#Cria grupo v0
v0=set( (1,1,2,3,5,8,13) )
#Cria grupo v1
v1=set( (2,3,5,7,11,13) )

# União
print v0 | v1
# Intersecção
print v0 & v1
# Diferença
print v0 - v1
#Diferença simétrica
print v0 ^ v1
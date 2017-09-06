# -*- coding: utf-8 -*-
# esse dicionario e simples porém muito bom para guardar conjunto de chave valores

print "Exemplo 1"
# cria um dicionario utilizando chave valor dentro de { }
DicionarioDelinguagens = {'angular':'Angular é um framework da google','react':'React é um framework do facebook'}

#imprimir dicionario inteiro
print DicionarioDelinguagens

# imprimi apenas as chaves angular e react
print DicionarioDelinguagens.keys()
#ordenar dicionario, porem temos que guardar uma lista do dicionario
print "Ordenar Lista de Keys"
lista = DicionarioDelinguagens.keys()
lista.sort()
print lista
# Para verificar a existência de uma chave, utilize o método has_key()
print "Existe Angular no Dicionario: "+ str(DicionarioDelinguagens.has_key("angular"))


print "\nExemplo 2"
# outra forma de declarar com dict o dicionario
DicionarioDelinguagens2 = dict([('angular', 'Angular é um framework da google'), ('React', 'React é um framework do facebook')])
print DicionarioDelinguagens2
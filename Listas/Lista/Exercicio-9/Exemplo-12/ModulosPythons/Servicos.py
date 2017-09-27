# -*- coding: UTF-8 -*-
# Autor: Rafael Viana


import requests

def cep(x):
    return requests.get('http://viacep.com.br/ws/'+x+'/json/unicode/').json()


print cep('79400000')
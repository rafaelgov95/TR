# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

import datetime
import requests

# agora = lambda: datetime.date.today().strftime('%d/%m/%Y')
# bitcoin = lambda: float("{0:.4f}".format(float(requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/').json()['ticker']['sell'])))

# Valores = lambda x:

def cep(self,x):
   return requests.get(str('http://viacep.com.br/ws/',x,'/json/unicode/')).json()

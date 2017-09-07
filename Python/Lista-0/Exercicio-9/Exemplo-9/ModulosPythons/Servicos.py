# -*- coding: UTF-8 -*-

import datetime
import requests

agora = lambda: datetime.date.today().strftime('%d/%m/%Y')
bitcoin = lambda: float("{0:.4f}".format(float(requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/').json()['ticker']['sell'])))


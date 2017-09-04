# -*- coding: UTF-8 -*-

import datetime

Diasemana = ('segunda feira','terceira feira','quarta feira',
             'quinta feira','sexta feira','sabado','domingo')
Meses=('janeiro','fevereiro','mar','abril','maio','junho',
       'julho','agosto','setembro','outubro','novembro','dezembro')

# agora = datetime.date.today()
agora = lambda:  datetime.date.today().strftime('%d/%m/%Y')

# aniversario =datetime.date(1971,12,23)

# mes=(agora.month-1)
# diadoano=(agora.strftime('%j'))
# diadasemana = datetime.date.weekday(agora)
# print 'Hoje e dia:', agora.strftime('%d/%m/%Y')
# print 'Aniversario:', aniversario.strftime('%d/%m/%Y')
# print 'Hoje e:' ,Diasemana[diadasemana]
# print 'Mes:', Meses[mes]
# print 'Somando-se 2 dias:', (agora + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
# print 'Somando-se 2 semanas:', (agora + datetime.timedelta(weeks=2)).strftime('%d/%m/%Y')
# print 'Somando-se 3 meses:', (agora + datetime.timedelta(days=90)).strftime('%d/%m/%Y')
# print 'Somando-se 1 ano////////;:', (agora + datetime.timedelta(days=365)).strftime('%d/%m/%Y')
# idade=(agora - aniversario)
# print 'Idade:', (idade.days)/365 , 'To ficando velho'
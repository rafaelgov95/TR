# -*- coding: UTF-8 -*-
# Autor: Rafael Viana

u =  u"äöü"
s = u.encode('utf8')

print s ## Resultado : äöü.

## Injetando code UTF-8 direto em line.
print '\xe2\x82\xac\xe2\x82\xac\xe2\x82\xac' ## Resultado : €€€.
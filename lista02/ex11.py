from datetime import date, datetime

mesIni = int(input('Digite o mês inicial: '))
anoIni = int(input('Digite o ano inicial: '))
mesFin = int(input('Digite o mês final: '))
anoFin = int(input('Digite o ano final: '))

if anoFin < anoIni or mesIni > 12 or mesIni < 1 or mesFin > 12 or mesFin < 1:
    print('Impossível realizar o cálculo. Anos e/ou meses incosistentes.')
    quit()
elif mesFin % 2 == 1 or mesFin == 12:
    data_final = date(year=anoFin, month=mesFin, day=31)
elif mesFin == 2:
    data_final = date(year=anoFin, month=mesFin, day=28)
elif mesFin % 2 == 0 and mesFin != 12:
    data_final = date(year=anoFin, month=mesFin, day=30)

data_inicial = date(year=anoIni, month=mesIni, day=1)
data_diff = data_final - data_inicial
data_format = str(data_diff)
data_format = data_format.split(' ')[0]
idade = int(data_format)
print(f'A idade desta pessoas em dias é: {idade+1}')
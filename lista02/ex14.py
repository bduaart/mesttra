from datetime import date, datetime

diaFin = int(input('Digite o dia final: '))
mesFin = int(input('Digite o mês final: '))

if (diaFin < 1 or diaFin > 31 or mesFin < 1 or mesFin > 12) or (mesFin == 2 and diaFin > 28) or (mesFin % 2 == 1 and diaFin > 31):
    print('Impossível realizar o cálculo. Anos e meses incosistentes.')
    quit()
if mesFin % 2 == 0 and mesFin != 12 and diaFin > 30:
    print('Impossível realizar o cálculo. Anos e meses incosistentes.')
    quit()
else:
    data_ini = date(day=1, month=1, year=2021)
    data_fin = date(day=diaFin, month=mesFin, year=2021)
    data_diff = data_fin - data_ini
    data_format = str(data_diff)
    data_format = data_format.split(' ')[0]
    qtdDias = int(data_format)
    print(f'Quantidades de dias: {qtdDias+1}')
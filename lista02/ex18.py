salHoras = int(input('Digite a quantidade total da horas normais: '))
salExtra = int(input('Digite a quantidade total de horas extras: '))
adicional = int(input('Digite a quantidade total de dependentes menores que 6 anos: '))
if adicional > 3:
    print(f'Salário calculado para apenas 3 dependentes. Os demais {adicional-3} não receberão o auxílio.')
    adicional = 3

salHoras *=10.0
salExtra *= 15.0
adicional = adicional*90.0
salLiq = abs((salHoras*11 / 100) - salHoras)
print(f'Horas normais: R${salHoras:.2f}\n' 
+ f'Adicional de horas extras: R${salExtra:.2f}\n'
+ f'Adicional de dependentes: R$ {adicional:.2f}\n'
+ f'Salário Líquido (Hrs normais - Desconto): R${salLiq:.2f}\n'
+ f'Salário final {salLiq+salExtra+adicional:.2f}')

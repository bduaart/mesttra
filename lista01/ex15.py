lata_350ml = int(input('Digite a quantidade de latas de 350ml: '))
garrafa_600ml = int(input('Digite a quantidade de garrafas de 600ml: '))
garrafa_2lt = int(input('Digite a quantidade de garrafas de 2lts: '))

print(f'A quantidade total é {(lata_350ml*350 + garrafa_600ml*600 + garrafa_2lt*2000)/1000} litros')
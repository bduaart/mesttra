lata_350ml = int(input('Digite a quantidade de latas de 350ml: '))
garrafa_600ml = int(input('Digite a quantidade de garrafas de 600ml: '))
garrafa_2lt = int(input('Digite a quantidade de garrafas de 2lts: '))

print(f'A quantidade total é {int((lata_350ml*350 + garrafa_600ml*600 + garrafa_2lt*2000)/1000)} litros')

if garrafa_600ml*0.6*0.09 >= lata_350ml*0.35*0.15:
    print(f'Considere substituir a compra de {lata_350ml} latas de 350ml por {(lata_350ml*350) / 600:.2f} garrafas de 650ml e oferecer uma promoção.')
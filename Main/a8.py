speed = float(input('Qual é a velocidade atual do carro? '))
if speed > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (speed-80) * 7
    print('Você deve pagar uma multa de \033[33mR${:.2f}!'.format(multa))
print('\033[32mTenha um bom dia! Dirija com segurança!')
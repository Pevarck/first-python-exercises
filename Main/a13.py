salary = float(input('Qual é o salário do funcionário? R$'))
if salary <= 1250:
    novo = salary + (salary * 15 / 100)
else:
    novo = salary + (salary * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salary, novo))
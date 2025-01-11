preço = float(input('preço do produto: R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${:.2f}, com 5% de desoncto vai custar R${:.2f}'.format(preço, novo))

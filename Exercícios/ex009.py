larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
print('dimensão da parede de {}x{} e sua area é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('para pintar a parede, precisará de {}l de tinta.'.format(tinta))
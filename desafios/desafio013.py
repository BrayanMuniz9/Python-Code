n = input('Nome do funcionario: ')
s = float(input('Salario atual do funcionario: R$ '))
a = s * 0.15
sn = a + s
print(f'O salario de {n} que era R$ {s:.2f}, foi aumentado para R$ {sn:.2f}, assim tendo um aumento salarial de'
      f' R$ {a:.2f}.')

nome = input('Nome do aluno: ')
n1 = float(input('Nota do primeiro semestre: '))
n2 = float(input('Nota do segundo semestre: '))
t = n1 + n2
m = t / 2
g = (n1 + n2) / 2
print(f'A média do aluno {nome}, é de {g:.1f}')

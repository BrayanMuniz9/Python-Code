carro = input('Qual veiculo e marca: ')
kms = float(input('Quantos KMs percorrido com o veiculo?: '))
dias = int(input('Quantos dias o cliente ficou com o veiculo?: '))
print(f'O aluguel do {carro} que rodou {kms:.2F} KMs em {dias} dias ficou no total de R$ {(kms*0.15)+(dias*60):.2f} ')

print('Digite a altura do cliente: ')
altura = float(input())
print('Digite o sexo da pessoa: ')
sexo = input()

if sexo == 'M':
    peso = (72.7 * altura) - 58
else:
    if sexo == 'F':
        peso = (62.2 * altura) - 44.7

print(f'Peso ideal = {peso}')
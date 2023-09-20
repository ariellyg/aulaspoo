from random import randint
num = int(input('diga-me um numero:'))
x =0
for i in range(num + 1):
    x+= randint(1,10)

print(f'A soma dos valores deu {x}')


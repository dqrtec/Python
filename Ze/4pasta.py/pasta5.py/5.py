n = 0
cont = 0
maior = 0
print('*****Programa que imprime o maior número dentre os digitados*****')
while n >= 0:
	n = int(input('Digite um número negativo para sair do programa.\nDigite um número positivo:'))
	if n >= 0:
		if n > maior:
			maior = n
	cont = cont + 1

if cont == 0:
	print('Você não digitou nenhum número.')	
else:
		print('O maior número é', maior)
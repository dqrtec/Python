n = int(input('Digite um número para ser calculado o seu fatorial:'))
fatorial = 1
for i in range(1, n+1):
	fatorial = fatorial*i
print('O fatorial é', fatorial)
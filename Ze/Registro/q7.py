propina=[]
partido=[]
total=[]

'''data do pagamento, o valor da propina, a descrição da obra relacionada a propina, o
nome do político que recebeu a propina e a sigla do seu partido.
'''
cadastrar=True
while cadastrar:
	data=input("Digite a data do pagamento ")
	valor=float(input("Digite o valor da propina "))
	obr=input("Drescrição da obra ")
	nome=input("Nome do politico ")
	sigla=input("Digite a sigla do partido ")
	sigla.upper()

	if sigla in partido:
		print("",end="")
	else:
		partido.append(sigla)

	propina.append({"data":data,"valor":valor,"obra":obr,"nome":nome,"sigla":sigla})

	menu=input("Deseja cadastrar outra propina?(s/n)")
	if menu=="n":
		cadastrar=False

for i in range(len(partido)):
	valor_apurado=0
	for j in range(len(propina)):
		if partido[i]==propina[j]["sigla"]:
			valor_apurado+=propina[j]["valor"]
	total.append(valor_apurado)
maior=max(total)
for i in range(len(partido)):
	if total[i]==maior:
		indice=i
print("maior participação ",partido[indice])

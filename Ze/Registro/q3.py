loja=[]
'''código, a descrição, o valor e a quantidade em estoque
de 10 produtos'''
for i in range(9):
	loja.append([])
	cod=int(input("Digite o id do produto %d "%(i+1)))
	desc=input("Digite descrĩção do produto %d "%(i+1))
	valor=float(input("Digite o valor do produto %d "%(i+1)))
	estoque=int(input("Digite o estoque do produto %d "%(i+1)))
	loja[i].append(cod)
	loja[i].append({"descricao":desc,"valor":valor,"estoque":estoque}) 
	print("\n")
print("\n",)
print(sorted(loja[:]["id"]))
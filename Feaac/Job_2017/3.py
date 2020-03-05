def pesquisa_lista(lista, numero):
	i=0
	for x in lista:
		if numero==x:
			print("Numero na posicao ",i)
		
		i=i+1


alturas=[9,8,7,6,1,2,4,3,5,3]
pesquisa_lista(alturas,44)

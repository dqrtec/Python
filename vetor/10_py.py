tabela=[]
apurado = 0
for i in range(0,4):
    print("mercadoria ",i+1)
    preco=float(input("valor da mercadoria "))
    quantidade=float(input("quantidade vendida "))
    lucro = preco* quantidade
    tabela.append([preco,i,quantidade,lucro])
for i in range(0, 4):
    apurado=apurado+tabela[i][3]
print(apurado)

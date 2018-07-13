x=[]
y=[]
produto=0
n = int(input("tamanho dos vatores "))

for i in range(0,n):
    x.append(float(input("digite um valor do vetor de x")))
    y.append(float(input("digite um valor do vetor de y")))

for i in range(0,n):
    produto=produto+(x[i] * y[i])

print("produto escalar",produto)

coeficientes=[]
x=[]
p=[]
soma=0

#entrar com os valores
n = int(input("digite n"))
for i in range(0,(n+1)):
    print("digite o",i,"º  coeficiente",end=" ")
    coeficientes.append(float(input("")))
for i in range(1,11):
    print("digite o",i,"º  valor de x",end=" ")
    x.append(float(input("")))

#calcular p
for i in range(0,10): #i = valor de x
    soma = 0
    for j in range(0,(n+1)): #j = p de x
        soma= soma+ (coeficientes[j]*(x[i]**j))
    p.append(soma)

#saidas
for i in range(0,10):
    print("valor de x:",x[i],", valor de P[x]:",p[i])

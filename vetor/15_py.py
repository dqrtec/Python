n = int(input("Digite n "))
soma=0
valores=[]
variancia = 0
desvio = 0

#   recebe os numeros e adiciona no somatorio
for i in range(0, n):
    numemro = float(input("numero "))
    valores.append(numemro)
    soma=soma+numemro

media = soma/n
for i in range(0,n):
    variancia= variancia + (valores[i]-media)**2
variancia = variancia/(n-1)#    variancia
desvio = variancia ** (1/2)#    desvio

print("media:", media)
print("variancia:", variancia)
print("desvio:", desvio)

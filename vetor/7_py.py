from random import *
temperaturas=[]
menor = 0
soma=0
temp=0
maior = 0
cont = 0
media =0

for dia in range(0,120):
    temp = randint(15,40)
    soma+=temp
    temperaturas.append(temp)
    if menor ==0 or temperaturas[dia]<menor:
        menor = temperaturas[dia]
    if temperaturas[dia]>maior:
        maior = temperaturas[dia]
print("maior temperatura ",maior)
print("maior temperatura ",menor)
media = float(soma/121)
print("media ",media)
for dia in range(0,120):
    if media>temperaturas[dia]:
        cont+=1
print("numeros abaixo da media", cont)

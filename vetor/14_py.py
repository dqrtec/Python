alturas=[9,8,7,6,1,2,4,3,5,3]
print(alturas)
menor=100
indice=0

for j in range(0, len(alturas)):
    for i in range(j, len(alturas)):
        if alturas[i]<menor:
            menor=alturas[i]
            indice=i
    #alturas.pop(i)
    del(alturas[indice])
    alturas.insert(j, menor)
    print(alturas)
    menor=100
print(alturas)


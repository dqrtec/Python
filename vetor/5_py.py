a= 0
sequencia = []
sequencia.append(1)

aux = 0
for i in range(1,50):
    aux = a
    a= sequencia[i-1]
    sequencia.append(sequencia[i-1]+aux)
print(str(sequencia).lstrip('[').rstrip(']'))

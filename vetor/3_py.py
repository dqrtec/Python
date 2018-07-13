lista = []
for numeros in range(1 , 20 , 2):
    lista.append(numeros*numeros)
print(str(lista).lstrip('[').rstrip(']'))

numeros = []
for multiplo in range(1 , 500):
    if multiplo % 5 == 0:
        numeros.append(multiplo)
print(str(numeros).lstrip('[').rstrip(']'))
        

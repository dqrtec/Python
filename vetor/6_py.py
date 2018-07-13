import math 
lista = []
divisor=3
fat = 1
somatorio = 0
x = (float(input("Digite um ângulo em graus para calcular seu seno:"))*math.pi)/180
lista.append(x)
somatorio=somatorio+x

for i in range(1, 15):
    
    for j in range(1,divisor+1):
        fat = fat*j
        
    if i%2==0:
        somatorio=(somatorio+(x**divisor)/fat)
        lista.append((x**divisor)/fat)
    else:
        somatorio= somatorio - ((x**divisor)/fat)
        lista.append(-1*((x**divisor)/fat))
    
    divisor=divisor+2
    fat=1
print(somatorio)
print(lista)

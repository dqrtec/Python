cordenada=[]
raios=[]
adiciona = True
raio=0
aux_x=0
aux_y=0
x =float(input("digite o valor de x central "))
y =float(input("digite o valor de y central "))
n =int(input("digite o numeros de pontos que será fornecido "))

#Recebe valores dos pontos
for i in range(0,n):
    print(i+1,"º cordenada")
    aux_x = float(input("x "))
    aux_y = float(input("y "))
    cordenada.append([aux_x,aux_y])
    
for i in range(0, n):
    raio=( ((x-cordenada[i][0])**(2)) + ((y-cordenada[i][1])**2) ) ** (1/2)
    for j in range(0,len(raios)):
        if raios[j]==raio and adiciona==True:
            adiciona=False
    if adiciona==True:
        raios.append(raio)
    adiciona=True
print(str(raios).lstrip('[').rstrip(']'))

#Escreva um programa que determine as componentes conexas do grafo não-direcionado recebido como entrada.

input("")
input("")
n = int(input("").split("=")[1])
input("")
listaAdjacencia = []
atingido = []
 
for i in range(1,n+2):
  listaAdjacencia.append([])
  atingido.append(0)

while True:
  try:
    aux = input("")
    x1 , x2 = aux.split(" ")
    listaAdjacencia[int(x1)].append(int(x2))
    listaAdjacencia[int(x2)].append(int(x1))
  except:
    break

 
componenteConexa = []
fila = []
for i in range(1,n+1):
  if(atingido[i] == 0):
    atingido[i] = 1
    #componenteConexa.append(i)
    fila.append(i)
    while(len(fila) > 0):
      j = fila.pop()
      componenteConexa.append(j)
      for vizinho in listaAdjacencia[j]:
        if( atingido[vizinho] == 0 ):
          atingido[vizinho] = 1
          fila.append(vizinho)
          
    ordem = sorted(componenteConexa)
    componenteConexa = []
    for inteiro in ordem:
      componenteConexa.append(str(inteiro))
      
    print(' '.join(componenteConexa))
    
    componenteConexa = []
    fila = [] 

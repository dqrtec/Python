#Escreva um programa que determine as componentes conexas do grafo não-direcionado recebido como entrada.

#Quantidadde de aresstas
n = int(input("").split("=")[1])

listaAdjacencia = []
atingido = []

#Melhoria
#[ [] for i in range(1,n+2)]
for i in range(1,n+2):
  listaAdjacencia.append([])
  atingido.append(False)

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
  if(atingido[i] == False):
    atingido[i] = True
    fila.append(i)
    while(len(fila) > 0):
      j = fila.pop()
      componenteConexa.append(j)
      for vizinho in listaAdjacencia[j]:
        if( atingido[vizinho] == False ):
          atingido[vizinho] = True
          fila.append(vizinho)
          
    ordem = sorted(componenteConexa)
    componenteConexa = []
    for inteiro in ordem:
      componenteConexa.append(str(inteiro))
      
    print(' '.join(componenteConexa))
    
    componenteConexa = []
    fila = [] 
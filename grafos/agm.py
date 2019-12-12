#Escreva um programa que determine as componentes conexas do grafo não-direcionado recebido como entrada.

def entradaInicial():
  input()
  input()
  n = int(input("").split("=")[1])
  input()
  return n

class Vertice(object):
  def _init_(self):
    self.componenteDoVertice = ComponenteConexas(self)

class ComponenteConexas(object):
  def _init_(self, vertice):
    self.QuantiadeVertices = 1
    self.listaVertices = [vertice]

  def juntarComponente(self, componenteMenor):
    self.listaVertices = self.listaVertices + componenteMenor.listaVertices
    self.QuantiadeVertices = self.QuantiadeVertices + componenteMenor.QuantiadeVertices

    for elementoComponenteConexaMenor in componenteMenor.listaVertices:
      elementoComponenteConexaMenor.componenteDoVertice = self


#componenteAtual = 0



#componentesConexas=[]
#for i in range(0,n+1):
#  componentesConexas.append([])
def criaVertices():
  listaVerticesEntradaN =[]
  for i in range(0,n+1):
    listaVerticesEntradaN.append(Vertice())
  return listaVerticesEntradaN

def recebearestasPonderadas():
  heap=[]
  while True:
    try:
      a = input().split(" ")
      a0 = int(a[0])
      a1 = int(a[1])
      a2 = float(a[2])
      heap.append( [ a2 , [ a0 , a1 ] ] )
    except:
      break;
  heapOrdenada = sorted(heap)
  return heapOrdenada

def somaAGM(n, heap):
  interadorListaArestas = 0
  soma = 0
  QtdArestasColocadas= 0
  while QtdArestasColocadas < n-1:
    aresta = heap[interadorListaArestas]
    #heap.remove(aresta)
    no1 = aresta[1][0]
    no2 = aresta[1][1]
    peso = aresta[0]
    if( no1 is no2 ):
      

    #if( (componentesConexas[ no1 ] != componentesConexas[ no2 ]) or (componentesConexas[ no1 ] == []) ):
    #    soma +=  peso
    #    QtdArestasColocadas += 1
    #    componenteAtual += 1
    #    if(componentesConexas[ no1 ]==[] and componentesConexas[ no2 ]==[]):
    #      componentesConexas[no1] = [componenteAtual]
    #      componentesConexas[no2] = [componenteAtual]
    #    elif(componentesConexas[ no1 ]==[]):
    #      componentesConexas[ no1 ] =  componentesConexas[no2]
    #    elif(componentesConexas[ no2 ]==[]):
    #      componentesConexas[ no2 ] =  componentesConexas[no1]
    #    else:
    #      mudar1 = componentesConexas[no1]
    #      mudar2 = componentesConexas[no2]
    #      for j in range(1,n+1):
    #        if( (componentesConexas[j] == mudar1) or (componentesConexas[j] == mudar2) ):
    #          componentesConexas[j] = [componenteAtual]
  return soma


n = entradaInicial()

#Escreva um programa que determine a soma das arestad de que gera uma componente conexa.

def entradaInicial():
  n = int(input("").split("=")[1])
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
    no1 = aresta[1][0]
    no2 = aresta[1][1]
    peso = aresta[0]
    if( no1 is no2 ):
  return soma

n = entradaInicial()
arestas = recebearestasPonderadas()
resultado = somaAGM(n, arestas)
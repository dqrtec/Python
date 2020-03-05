import copy
def entrar_notas():
    n=[]
    print("Digite as notas")
    while True:
        i = input()
        if not i:
          break
        n.append(float(i))
    return n

def calcular_media(lista): # "lista" é a lista com as notas
    nova_lista=copy.copy(lista)
    soma=0
    i=0
    for val in enumerate(nova_lista):
        soma=soma+nova_lista[i]
        i=i+1
    media=soma/len(nova_lista)
    return media

def relatorio_notas():
    lista = copy.copy(entrar_notas())
    media=calcular_media(lista)

    for val in lista:
        print("Nota: ",val)
    print("Media da turma: ",media)


relatorio_notas()

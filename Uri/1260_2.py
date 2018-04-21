time = int(input())
lixo = input()  
lista = []
qtd = 0
for i in range(time):
    aux = input()
    total = 0
    if aux != '':
        while aux !='':
            total+=1
            lista.append(aux)
            aux = input()
        lista.sort()
        while len(lista) != 0:
            print("entrou")
            qtd = lista.count(lista[0])
            print("%s %0.4f"%(lista[0],(100*qtd/total)))
            for j in range(qtd):
                lista.remove(lista[0])
        print()

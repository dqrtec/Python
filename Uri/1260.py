import cmd 
cmd.prompt()
n = int(input())
for teste in range(n):
    print("")
    achou = 0
    lista = []
    contador = 0
    while(achou != 1):
        aqui = 0
        aux = input()
        if (aux == ""):
            achou = 1
        elif(len(lista) == 0):
            lista.append([aux,1])
            contador +=1
        else:
            for i in range(contador):
                if(lista[i][0]==aux):
                    lista[i][1] = lista[i][1] + 1
                    aqui = 1
            if(aqui==0):
                lista.append([aux,1])
                contador+=1
            aqui = 0
    print(lista)
    print(lista[0].sort())

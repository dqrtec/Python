a=input("Digite um texto com sufixos ")
b=a.split(" ")
partes=len(b)

while partes>0:
    for i in range(len(b[partes-1])-1):
        if b[partes-1][i]=="-":
            print(b[partes-1][i:])
    partes-=1

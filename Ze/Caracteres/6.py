a=input("Digite o valor Um texto com prefixos ")
b=a.split(" ")
partes=len(b)

while partes>0:
    for i in range(len(b[partes-1])-1):
        if b[partes-1][i]=="-":
            print(b[partes-1][0:i])
    partes-=1

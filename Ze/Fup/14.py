vet=[9,1,7,2,5,3,4,8,6]

def hanoi(n,m):
    if n>0:
        if m>1:
            if vet[m-1] > vet[m-2]:
                aux = vet[m-2]
                vet[m-2] = vet[m-1]
                vet[m-1] = aux
            return hanoi(n, m-1)
        else:
            return hanoi(n-1, len(vet))

    else:
        return 0

hanoi(len(vet),len(vet))
print(vet)

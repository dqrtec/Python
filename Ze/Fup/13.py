vet=[1,2,3,4,5,6,7,8,9]
def inverte(metade,n):
    if metade>=0:
        aux = vet[n-1]
        vet[n-1] =vet[len(vet)-n]
        vet[len(vet)-n] = aux
        return inverte(metade-1 , n-1)
    else:
        return 0
        
inverte( int(len(vet)/2) , len(vet))
print(vet)

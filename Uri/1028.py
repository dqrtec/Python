def ordena(x,y):
    if(x<y):
        aux = x
        x = y
        y = aux
    return x,y

times = int(input())
for i in range(times):
    n1 , n2 = input().split(' ')
    n1 = int(n1)
    n2 = int(n2)
    while abs(n1-n2)!=0:
        n1 , n2 = ordena(n1,n2)
        n1 = n1-n2
    print(n1)

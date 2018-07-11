def soma(n):
    if n>0:
        return soma(n-1)+n
    else:
        return 0

n = int(input("Digite o valor de N "))
print(soma(n))


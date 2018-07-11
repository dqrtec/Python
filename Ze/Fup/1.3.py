def soma(i,j):
    if j > 0:
        return soma(i,j-1)+1
    else:
        return i

x = int(input("Digite o primeiro numero "))
y = int(input("Digite o segundo numero "))
print(soma(x,y))

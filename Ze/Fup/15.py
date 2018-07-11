a=input("Digite uma palavra ")

def palindromo(vezes,n):
    if vezes>0:
        if a[len(a)-n] == a[n-1]:
            return palindromo(vezes-1 , n-1)
        else:
            return "Nao  e um palindromo"
    else:
        return "É um palindromo"


print( palindromo(int(len(a)/2), len(a)) )

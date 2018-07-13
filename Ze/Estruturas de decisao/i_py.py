a = float(input("Digite o valor de a "))
b = float(input("Digite o valor de b "))
c = float(input("Digite o valor de c "))
delta = ((b*b) - (4*a*c))

if delta >= 0:

    raiz1 = (((-b) + (delta**1/2))/(2*a))
    print("Primeira raiz = ",raiz1)
    raiz2 = (((-b) - (delta**1/2))/(2*a))
    print("Segunda raiz = ",raiz2)

else:

    prfloat("Não existe raiz no conjunto dos Reais.")

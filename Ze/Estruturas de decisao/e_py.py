investimento = int(input("Escolha seu tipo de investimento\n1 - Poupança\n2 - Fundo de Renda Fixa"))
valor = float(input("Valor a ser investido? "))

if investimento == 1:

    rendimento = valor*0.1

elif investimento == 2:

    rendimento = valor*0.15

else:

    print("Tipo inválido")

print("Rendimento a.m de = ", rendimento)

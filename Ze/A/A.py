numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
escolha = int(input("Qual dessas funções voce deseja fazer?\n1.Media\n2.Diferenca\n3.Produto\n4.Divisao"))

if escolha == 1:

    print("Media = ", (numero1+numero2)/2)

elif escolha == 2:

    if numero1>numero2:

        print("Diferenca = ", numero1-numero2)

    elif numero2>numero1:

        print("Diferença = ", numero2-numero1)

elif escolha == 3:

    print("Produto = ", numero1*numero2)

elif escolha == 4:

    if numero2 == 0:

        print("Nao existe divisão por 0")

    elif numero2 != 0:

        print('Divisao = ', numero1/numero2)

else:

    print('ENTRADA INVÁLIDA!')
        
    

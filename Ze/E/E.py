investimento = int(input('Programa que calcula o rendimento mensal para cada tipo de investimento\nDigite:\n1 para Poupança\n2 para Fundo de renda fixa\n'))
valor = float(input('Digite o valor a ser investido:\n'))
if investimento == 1:
    valor_corrigido = valor*0.1
elif investimento == 2:
    valor_corrigido = valor*0.15
else:
    print ('Opção de tipo de investimento inválida')

print ('Rendimento Mensal:', valor_corrigido)

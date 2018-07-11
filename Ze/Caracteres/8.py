from itertools import combinations 
cadeia = input("Digite um texto ")
n=int(input("Digite o valor de n "))
sub=[]
for tamanho in range(0,n+1):
  for combi in combinations(cadeia,tamanho):
    sub.append(combi)

print(sub)
questoes = 30
alunos = []
gabarito =[]
quantidade = int(input("quantos alunos "))
aux=0
pontos = 0

#recebe gabarito
for i in range(0, questoes):
    gabarito.append(input("digite o gabarito "))

# recebe matricula, resostas 
for i in range(0, quantidade): # i - aluno
    aux = [input("Digite sua matricula")]
    alunos.append(aux)
    for j in range(0, questoes): # j - questoes
        aux2=input("Digite o item ")
        alunos[i].append(aux2)
        if gabarito[j]==aux2:
            pontos= pontos+1
    alunos[i].append(pontos)
    pontos=0
    
#imprime resultados
for i in range(0, quantidade):
    print("matricula", alunos[i][0], " nota ->",  alunos[i][31])

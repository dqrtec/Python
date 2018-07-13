candidatos=[]
tem=False
voto=""
rodar=True
#encontrou=False
n = int(input("Quantos candidatos existem? "))
eleito=0
maior=0

for i in range(0, n):
    candidatos.append([input("Nome do candidato "), 0])

while rodar:
    voto= input("Qual o seu voto? ")
    if voto=="fim":
        rodar = False
    else:
        for i in range(0, n):
            if voto==candidatos[i][0]:
                candidatos[i][1]=candidatos[i][1]+1

for i in range(0,n):
    if candidatos[i][1]>maior:
        maior=candidatos[i][1]
        eleito=i
        
print(candidatos[eleito][0], " Foi eleito com:", candidatos[eleito][1], "votos")

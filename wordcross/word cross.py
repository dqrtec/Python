n = int(input("quantas letras tem a palavra?"))
letras = input("letras possiveis? (separados por virgula)").split(",")


sei = [(0, 'c'), (1, 'a')]

sei = []
print("Digite as letras que são conhecidas")
while True:
    try:
        pos = int(input("posicao da letra?"))
        letra = input("letra ?")
        sei.append( (pos,letra) )
        print( sei )
    except:
        break

print(sei)

print("")
print("Buscando ....")

i = open("palavras.txt")

index = 0

maximo = 320139

for d in range(maximo):
    try:
        
        l = i.readline()
        index += 1
        palavra = l.lower()
        palavra.replace(" ","")
        palavra = palavra[:-1]
        
        if len(palavra) == n:
            
            contador = 0
            contador_acertos = 0
            for j in range(len(palavra)):
                letra = palavra[j]
                if letra in letras:
                    contador += 1
            if contador == n:
                for s,e in sei:
                    if palavra[s] == e:
                        contador_acertos += 1
            
            if contador_acertos == len(sei):
                print(palavra)
    except:
        pass
print("FIM")
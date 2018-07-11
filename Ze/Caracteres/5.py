texto=input("Digite um texto ")
caracter=input("Digite um caracter ")
ponteiro=0
while ponteiro<len(texto):
    if texto[ponteiro]==caracter:
        texto = texto[:ponteiro] + texto[ponteiro+1:]
    ponteiro+=1
print(texto)

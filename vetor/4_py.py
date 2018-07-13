maiores =[]
atletas =[]
soma=0
for i in range(0,10):
    atleta = float(input("Digie a altura"))
    soma+=atleta
    atletas.append( atleta)
media = soma /  10
print("Media: ",media)
for j in range(0,10):
    if atletas[j]>=media:
        maiores.append(atletas[j])
print("altura dos maiores que a media", str(maiores).lstrip('[').rstrip(']'))
    

sexo= input("Digite seu sexo \nM para Mmulher \n H para Homem ")
altura = float(input("Digite sua altura em metros "))
if((sexo != "M") | (sexo != "H")):
    if(sexo=="H"):
     calculo=((72.7*altura)-58)
     print( "o eso ideal é ", calculo)
    elif(sexo=="M"):
     calculo<-(62.1*altura)-44.7
     print( "o eso ideal é ", calculo)
else:
 print("Sexo não identificado")

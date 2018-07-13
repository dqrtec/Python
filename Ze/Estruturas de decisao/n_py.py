a = float(input("Digite o valor do primeiro lado"))
b = float(input("Digite o valor do segundo lado"))
c = float(input("Digite o valor do terceiro lado"))
	
if(((a+b)>c) & (a+c>b)) & (b+c>a):			
    if (((a==b)&(a==c)) | ((c==b)&(a==c))) | ((a==b)&(b==c)):
        print(" os lados sao de um triangulo equilatero")
    elif((a==b)|(a==c))|(b==c):
        print(" temos um triangulo isoceles")
    else:
        print(" O triangulo é escaleno")
else:
    print(" esses lados não sao capazes de construir um triangulo euclidiano ")
	

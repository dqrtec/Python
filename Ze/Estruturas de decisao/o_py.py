import math
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

if a>(b+c) and b>(a+c) and c>(a+b):

	print("Não sao lados de um triangulo.")

else:

	cosseno_a =(((a*a)-(b*b)-(c*c))/(-2*b*c))	
	angulo_a = math.degrees(math.acos(cosseno_a))

	cosseno_b =	((b*b)-(a*a)-(c*c))/(-2*a*c)	
	angulo_b = math.degrees(math.acos(cosseno_b)) 

	cosseno_c = ((c*c)-(a*a)-(b*b))/(-2*a*c)
	angulo_c = math.degrees(math.acos(cosseno_c))

	if angulo1>90 or angulo2>90 or angulo3>90:

		print("Triângulo Obtusângulo")

	elif angulo1==90 or angulo2==90 or angulo3==90:

		print("Triângulo Retângulo")

	elif angulo1<90 and angulo2<90 and angulo3<90:

		print("Triângulo Acutângulo")

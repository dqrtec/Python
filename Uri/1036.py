import math
def delta(a,b,c):
    return(b*b - 4*a*c)
    
a, b, c = input().split(' ')
a= float(a)
b= float(b)
c= float(c)

delta = delta(a,b,c)
if delta<0 or a== 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(delta) ) / (2*a)
    r2 = (-b - math.sqrt(delta) ) / (2*a)
    print("R1 = %0.5f\nR2 = %0.5f"%(r1,r2))

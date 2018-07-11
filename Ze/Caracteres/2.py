h=0
t=input("Digite uma palavra")
for i in range(0,int(len(t)/2)):
   if t[i] != t[len(t)-i-1]:
     h=1
if h==0:
  print("É um polindromo")
else:
  print("NÃO È um polindromo")
   

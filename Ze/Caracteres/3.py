t=input("Digite seu nome")
f=True
i=0
tamanho= len(t)-1
while f:
  if t[tamanho-1]==" ":
    i+=1
    print(t[tamanho:len(t)-1],",",t[0:tamanho])
    f=False
  tamanho=tamanho-1
  
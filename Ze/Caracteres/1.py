mai=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z']
min=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
t=input("Digite um texto ")
f=0
for i in range(len(t)):
  #print("i",i)
  for j in range(len(mai)):
    #print("j",j)
    if t[i]==mai[j]:
      f=1
      print(min[j],end="")
    elif t[i]==min[j]:
      f=1
      print(mai[j],end="")
  if f==0:
    print(t[i],end="")
  f=0

alfa=['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
letrast =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
letrast2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
t=input("Digite uma palavra ")
t2=input("Digite uma palavra a comparar ")
for i in range(len(t)):
    for j in range(len(alfa)):
        if alfa[j] == t[i]:
            letrast[j]=letrast[j]+1
        if alfa[j] == t2[i]:
            letrast2[j]=letrast2[j]+1

diferentes=0
print(letrast)
print(letrast2)
for i in range(len(letrast)):
    if letrast[i]!=letrast2[i]:
        diferentes+=1
if diferentes!=0:
    print("Não sao anagramas")
else:
    print("É um anagrama!")

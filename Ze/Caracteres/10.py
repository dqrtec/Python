senha=input("Digite uma senha")
ma=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z']
mi=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
di=['0','1','2','3','4','5','6','7','8','9']
qtd_mai=0
qtd_min=0
qtd_dig=0
if 8<=len(senha)<=15:
    for i in range(len(senha)-1):
        for j in range(len(ma)-1):
            if ma[j]==senha[i]:
                qtd_mai+=1
            elif mi[j]==senha[i]:
                qtd_min+=1
    for i in range(len(senha)-1):
        for j in range(len(di)-1):
            if senha[i]==di[j]:
                qtd_dig+=1
        
else:
    print("Quantidade invalida de caracteres")

if qtd_mai>0 and qtd_mai>0 and qtd_dig>0:
    print("Senha Valida")
else:
    print("INVALIDA!")

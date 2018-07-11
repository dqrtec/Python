ano=input("Digite o ano ")
unidade=["um","dois", "três","quatro", "cinco" ,"seis", "sete" ,"oito", "nove"]
dezenas=[" vinte e "," trinta e ", " quarenta e "," cinquenta e "," sessenta e "," setenta e "," oitenta e "," noventa e "]        

if ano[0]!="0":
    print(unidade[int(ano[0])-1]+" mil ",end=" ")
    
if ano[1]!="0":
    if ano[1]=="4" or ano[1]=="6" or ano[1]=="7" or ano[1]=="8" or ano[1]=="9":
        print( unidade[int(ano[2])-1]," centos e ",end=" ")
    elif ano[1]=="1":
        if ano[2]=="0" and ano[3]=="0":
            print(" cem")
        else:
            print("cento e ",end=" ")
    elif ano[1]=="2":
        print("duzentos e ",end=" ")
    elif ano[1]=="1":
        print("trezentos e ",end=" ")
    elif ano[1]=="5":
        print("quinhentos e ",end=" ")

if ano[2]!="0":
    if ano[2]=="1" and ano[3]=="0":
        print(" dez")
    elif ano[2]=="1" and ano[3]=="1":
        print(" onze")
    elif ano[2]=="1" and ano[3]=="2":
        print(" doze")
    elif ano[2]=="1" and ano[3]=="3":
        print(" treze")
    elif ano[2]=="1" and ano[3]=="4":
        print(" catorze")
    elif ano[2]=="1" and ano[3]=="5":
        print(" quinze")
    elif ano[2]=="1" and ano[3]=="6":
        print(" dezesseis")
    elif ano[2]=="1" and ano[3]=="7":
        print(" dezessete")
    elif ano[2]=="1" and ano[3]=="8":
        print(" dezoito")
    elif ano[2]=="1" and ano[3]=="9":
        print(" deznove")
    else:
        print(dezenas[int(ano[2])-2],end=" ")

if ano[3]!="0":
    print(unidade[int(ano[3])-1]," ",end=" ")

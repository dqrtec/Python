estados=["Acre","Alagoas","Amapá","Amazonas","Bahia","Ceará","Distrito Federal","Espírito Santo","Goiás","Maranhão","Minas Gerais","Mato Grosso do Sul","Mato Grosso","Pará","Paraíba","Pernambuco"  ,"Piauí","Paraná","Rio de Janeiro","Rio Grande do Norte","Rondônia","Roraima","Rio Grande do Sul","Santa Catarina","Sergipe","São Paulo","Tocantins"]

ar_relatorio=open("relatório.xlsx",'w')

###############################################################################

def opcao1():

    valida_uf=True
    rodou=0

    while valida_uf:

        print("___________________________")
        for i in range(len(estados)-1):
            print("|",uf_ufs[i]," | ",estados[i])
        print("|___________________________|\n")

        uf= input("Escolha um Estado pela UF >")
        uf=uf.upper()

        for i in range(len(uf_ufs)): 
            if uf_ufs[i] == uf:
                ar_relatorio.write("\nU\tCODIGO\tPOPULAÇÃO\tPIB\tPRIB PER CAPITA\n")
                ar_relatorio.write("%s\t%s\t%s\t%s\t%s\n\n"%(uf_ufs[i],codigos_ufs[i],populacao_ufs[i],pib_ufs[i],pib_populacao_ufs[i]))
                print("\nUF:",uf_ufs[i],"\nCODIGO:" ,codigos_ufs[i],"\nPOPULAÇÃO:", populacao_ufs[i],"\nPIB:", pib_ufs[i],"\nPRIB PER CAPITA:", pib_populacao_ufs[i])
                rodou=1

        if rodou==0:

            print("\tUF inválida! Escolha novamente")

        else:

            valida_uf=False

#####################################################################################

def opcao2():
    valida_escolha=True
    while valida_escolha:
         print("\nDigite os numeros dos campos que deseja visualizar(ex:23,nostra a pupulação e o pib)\n ______________________\n| 1 | Codigo          |\n| 2 | População       |\n| 3 | PIB             |\n|_4_|_PIB_PERCAPITA___|")     
         escolha=input("\n\t>>")

         if "1" in escolha or "2" in escolha or "3" in escolha or "4" in escolha:
             valida_escolha=False
             print("\nUF    ",end="")
             ar_relatorio.write("UF\t")
             if "1" in escolha:
                print("CODIGO    ",end="")
                ar_relatorio.write("CODIGO\t")
             if "2" in escolha:
                print("POPULAÇÃO    ",end="")
                ar_relatorio.write("POPULAÇÃO\t")
             if "3" in escolha:
                print("PIB    ",end="")
                ar_relatorio.write("PIB\t")
             if "4" in escolha:
                print("PIB PERCAPITA",end="")
                ar_relatorio.write("PIB PERCAPITA\t")
             print("")

             ar_relatorio.write("\n")

             for i in range(len(uf_ufs)):

                saida=str(uf_ufs[i])+"\t"
                ar_relatorio.write("%s\t"%(uf_ufs[i]))

                if "1" in escolha:

                     ar_relatorio.write("%s\t"%(codigos_ufs[i]))
                     saida = saida+ str(codigos_ufs[i])+"    "

                if "2" in escolha:

                     saida = saida+ str(populacao_ufs[i])+"    " 
                     ar_relatorio.write("%s\t"%(populacao_ufs[i]))

                if "3" in escolha:

                     saida = saida+ str(pib_ufs[i])+"    "
                     ar_relatorio.write("%s\t"%(pib_ufs[i]))

                if "4" in escolha:

                     saida = saida+ str(pib_populacao_ufs[i])+"    "
                     ar_relatorio.write("%s\t"%(pib_populacao_ufs[i]))

                print (saida)
                ar_relatorio.write("\n\n")
         else:
            print("Escolha um campo válido!")

########################################################################################
def opcao3(argumento):

    if argumento==1:

        return max(codigo_estatistico) , min(codigo_estatistico) , (sum(codigo_estatistico)/len(codigo_estatistico)) , "Codigo",variancia(codigo_estatistico),desvio(codigo_estatistico)

    elif argumento==2:

        return max(populacao_estatistico) , min(populacao_estatistico) , (sum(populacao_estatistico)/len(populacao_estatistico)) , "População",variancia(populacao_estatistico),desvio(populacao_estatistico)

    elif argumento==3:

        return max(pib_estatistico) , min(pib_estatistico) , (sum(pib_estatistico)/len(pib_estatistico)),"PIB",variancia(pib_estatistico),desvio(pib_estatistico)

    else:

        return max(pib_populacao_estatistico) , min(pib_populacao_estatistico) , (sum(pib_populacao_estatistico)/len(pib_populacao_estatistico)),"PIB Percapita",variancia(pib_populacao_estatistico),desvio(pib_populacao_estatistico)


######################################################################################

def variancia(entrada):

    media=sum(entrada)/len(entrada)
    soma=0
    variancia=0

    for i in entrada:
        soma+=(i-media)**2
    return soma/float(len(entrada)-1)

def desvio(entrada):

    return (variancia(entrada))**(1/2)

########################################################################################

import csv
from decimal import * 

########################################################################################

main=True
while main:

 ar = open('uf.txt') 
 csv_ar = csv.reader(ar, delimiter=";")
 linhas_arquivos = []
 uf_ufs = []
 codigos_ufs = []
 populacao_ufs = []
 pib_ufs = []
 pib_populacao_ufs = []
 
 codigo_estatistico=[]
 populacao_estatistico=[]
 pib_estatistico=[]
 pib_populacao_estatistico=[]
 
 for linha in csv_ar:
     linhas_arquivos.append(linha)
     uf_ufs.append(linha[0])
     codigos_ufs.append(linha[1])
     codigo_estatistico.append(float(linha[1]))
     populacao_ufs.append(linha[2])
     populacao_estatistico.append(float(linha[2]))
     pib_ufs.append(linha[3])
     pib_estatistico.append(float(linha[3]))
     pib_populacao_ufs.append(linha[4])
     pib_populacao_estatistico.append(float(linha[4]))

 menu=True
 while menu:
     menu=False
     opcao = input("\n\t\tEscolha uma das opções:\n \t _________________________________________________\n \t|                                                 |\n \t| 1 > Ver os dados de um estado                   |\n \t| 2 > criar uma tabela personalizada com os dados |\n \t| 3 > Ver estatísticas de uma variável            |\n \t|_________________________________________________|\n\t***Um arquivo cahamado 'Relatorio.xlsx' será gerado apos a execução do programa.***\n >>>")
 ########## OPÇÃO 1:
     if opcao=="1":
        opcao1()
 ########## OPÇÃO 2:
     elif opcao=="2":
        opcao2()
 ########## OPÇÃO 3:
     elif opcao=="3":
         print(sum(codigo_estatistico))
         valida_estatistica=True
         while valida_estatistica:
            estatistica = int(input("\tEscolha uma variável para visualizar seus dados estatísticos\n ______________________\n| 1 | Codigo          |\n| 2 | População       |\n| 3 | PIB             |\n|_4_|_PIB_PERCAPITA___|\n\t>>"))
            if estatistica==1 or estatistica==2 or estatistica==3 or estatistica==4:
                valida_estatistica=False
                maior , menor , media , campo , var , des = opcao3(estatistica)
                print("\n Campo :%s\n\tMaior Valor:%f\n\tMenor Valor:%f\n\tMédia:%f\n\tVariância:%s\n\tDesvio Padrão:%s"%(campo,maior,menor,media,var , des))
                ar_relatorio.write("\n Campo :%s\n\tMaior Valor:%f\n\tMenor Valor:%f\n\tMédia:%f\n\tVariância:%s\n\tDesvio Padrão:%s\n"%(campo,maior,menor,media,var , des))
            else:
                print("Opcação invalida.Tente novamente")
     else:
         print("Entrada inválida!")
         menu=True

 valida_decisao=True
 while valida_decisao:

     decisao=input("\n \t >Deseja fazer outra operação?(S/N)")
     decisao=decisao.upper()
     if decisao=="N":

        valida_decisao=False
        main=False
        ar_relatorio.close()

     elif decisao!="S":

        print("Entrada invalida")

     else:

        break

ar=open("relatorio.xls",'w')


######################## SAC
def sac(saldo,prazo,taxa,mes=0,total=0,juros=0):
    amortizacao=saldo/prazo
    saldo_final=saldo
    
    for times in range(prazo):
      saldo=saldo-(amortizacao+juros)
      mes+=1
      juros=amortizacao*taxa*(prazo-(times+1)+1)
      
      total+=juros
      print(" \n")
      prestacao= amortizacao+juros
      saldo_final-=amortizacao
      saldo=saldo_final+amortizacao
      ar.write("\n%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f" %(mes ,saldo,prestacao, amortizacao,juros,saldo_final))
      print ("%d ->    %0.2f    %0.2f    %0.2f    %0.2f    %0.2f" %(mes ,saldo,prestacao, amortizacao,juros,saldo_final))
    print("\n \t \t  O JUROS TOTAL É -> %0.2f"%(total))
    ar.write("\n \t \t  O JUROS TOTAL É ->   %0.2f "%(total))

######################## PRICE

def price(saldo,prazo,taxa,mes=0,total=0,juros=0):
    prestacao= ((saldo*taxa)/(1-(1+taxa)**(-prazo)))
    for t in range(prazo):
        juros=saldo*taxa
        amortizacao=prestacao-juros
        mes+=1
        saldo=(saldo-prestacao)+juros
        total+=juros
        print(" \n")
        saldo_inicial=saldo+amortizacao
        ar.write("\n%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\n" %(mes ,saldo,prestacao, amortizacao,juros,saldo_final))
        print ("%d ->    %0.2f    %0.2f    %0.2f    %0.2f    %0.2f" %(mes,saldo_inicial , prestacao, amortizacao, juros , saldo  ))
    print("\n \t \t  O JUROS TOTAL É ->   %0.2f "%(total))
    ar.write("\n \t \t  O JUROS TOTAL É ->   %0.2f "%(total))

######################
executar=True
while executar:

    print("\t\t _____________________\n\t\t|                     |\n\t\t|SIMULADOR IMOBILIÁRIO|\n\t\t|_____________________|\n ***Gera arquivo no final da execução***")
    print("")
    
    saldo_vazio=True
    while saldo_vazio:
        saldo=input(" Digite o Valor do imprestimo >")
        print("")
        if saldo=="":
            print("\tEntrada invalida")
            print("")
        else:
            saldo_vazio=False
            saldo= float(saldo)

    prazo_vazio=True
    while prazo_vazio:
        prazo=input(" Digite o prazo para quitar a divida(em meses) >")
        print("")
        if prazo=="":
            print("\tEntrada invalida, Nada foi digitado")
            print("")
        elif int(prazo)<=0:
            print("\tEntrada invalida, Numero menor que 1")
            print("")
        else:
            prazo_vazio=False
            prazo=int(prazo)

    j_vazio=True
    while j_vazio:
        j=input(" Digite a taxa de juros a.a% >")
        print("")
        if j=="":
            print("\tEntrada invalida, Nada foi digitado")
            print("")
        elif float(j)<=0:
            print("\tEntrada invalida de juros")
            print("")
        else:
            j_vazio=False
            j=float(j)
            
    taxa= (((1+(j/100))**(1/12)) -1)
    
    
    valida_menu=True
    while valida_menu:
        menu=input(" Escolha uma das opções de financiamento abaixo:\n\t ________________\n\t|\tmenu\t | \n\t|SAC(1)\t PRICE(2)|\n\t|________________|\n>")
        if menu=="1" or menu=="2":
            ar.write("PRINCIPAL = %f \t N = %d meses \t TAXA = %f%%(%f%% mês)\n"%(saldo,prazo,j,(taxa*100)))
            print("PRINCIPAL = %f , N = %d meses , TAXA = %f%%(%f%% mês)"%(saldo,prazo,j,(taxa*100)))
            print("\nMES    SALDO    PRESTAÇÃO    AMORTIZAÇÃO    JUROS    SALDO FINAL")
            ar.write("MES\tSALDO\tPRESTAÇÃO\tAMORTIZAÇÃO\tJUROS\tSALDO FINAL")
            if menu=="1":
                sac(saldo,prazo,taxa)
            elif menu=="2":
                price(saldo,prazo,taxa)
            
            valida_menu=False
        else:
            print("Opção invalida!")
##############
    ar.close()
##############
    print("")

    validacao_vazio=True
    while validacao_vazio:
        simulacao=input("\tO RELATORIO 'relatorio.txt' COM A SIMULAÇÃO DO FINANCIAMENTO FOI CRIADO \n\nDeseja fazer outra simulação?(s/n)>")
        if simulacao =="s":
            print(" ")
            validacao_vazio=False
        elif simulacao =="n":
            executar=False
            validacao_vazio=False
        else:
            print("Digite uma entrada valida!")


######################## SAC
def sac(saldo,prazo,taxa,mes=0,total=0,juros=0):
    amortizacao=saldo/prazo
    saldo_final=saldo
    
    for times in range(prazo):
      saldo=saldo-(amortizacao+juros)
      mes=mes+1
      juros=(prazo-(times+1)+1)*amortizacao*taxa
      
      total+=juros 
      print(" \n")
      prestacao= amortizacao+juros
      saldo_final-=amortizacao
      saldo=saldo_final+amortizacao
      print ("%d >>\t %0.2f   \t %0.2f \t %0.2f \t %0.2f \t %0.2f" %(mes ,saldo,prestacao, amortizacao,juros,saldo_final))
    print("\n \t \t  O JUROS TOTAL É >> %0.2f"%(total))

######################## PRIME

def prime(saldo,prazo,taxa,mes=0,total=0,juros=0):
    prestacao= (saldo*taxa)/(1-(1+taxa)**(-prazo))
    for t in range(prazo):
        juros=saldo*taxa
        amortizacao=prestacao-juros
        mes=mes+1
        saldo=(saldo-prestacao)+juros
        total+=juros
        print(" \n")
        saldo_inicial=saldo+amortizacao
        print ("%d >>\t %0.2f   \t %0.2f \t %0.2f \t %0.2f  \t %0.2f " %(mes,saldo_inicial , prestacao, amortizacao, juros , saldo  ))
    print("\n \t \t  O JUROS TOTAL É >>   %0.2f "%(total))

######################
executar=True
while executar:
    
    saldo_vazio=True
    while saldo_vazio:
        saldo=input("Digite o Valor do imprestimo ")
        if saldo=="":
            print("Entrada invalida")
        else:
            saldo_vazio=False
            saldo= float(saldo)

    prazo_vazio=True
    while prazo_vazio:
        prazo=input("Digite o prazo para quitar a divida ")
        if prazo=="":
            print("Entrada invalida, Nada foi digitado")
        elif int(prazo)<=0:
            print("Entrada invalida, Numero menor que 1")
        else:
            prazo_vazio=False
            prazo=int(prazo)

    j_vazio=True
    while j_vazio:
        j=input("Digite a taxa de juros a.a% ")
        if j=="":
            print("Entrada invalida, Nada foi digitado")
        elif float(j)<=0:
            print("Entrada invalida de juros")
        else:
            j_vazio=False
            j=float(j)
            
    taxa= (((1+(j/100))**(1/12)) -1)
    
    
    
    menu=input("menu 1->SAC\t 2->PRIME ")
    
    if menu=="1":
        print("MES\t SALDO  \t PRESTAÇÃO \t amortizacaoTIZAÇÂO\tJUROS \t saldo Final")
        sac(saldo,prazo,taxa)
    elif menu=="2":
        print("MES\t SALDO  \t PRESTAÇÃO \t amortizacaoTIZAÇÂO\tJUROS \t saldo Final")
        prime(saldo,prazo,taxa)

    print("")

    validacao_vazio=True
    while validacao_vazio:
        simulacao=input("Deseja fazer outra simulação?(s/n)")
        if simulacao =="s":
            print(" ")
            validacao_vazio=False
        elif simulacao =="n":
            executar=False
            validacao_vazio=False
        else:
            print("Digite uma entrada valida!")

        
    

while True:#fica repetindo o programa quantas vezes o usuario quiser
    valor=int(input("Digite O valor do imprestimo > "))
    prazo=int(input("Digite a quantidade de meses para quitar a divida > "))
    j=int(input("Digite o juros anual > "))
    escolha=input("Qual tidpo de financiamento você deseja?\n SAC(1) ou PRICE(2)")
    taxa= (((1+(j/100))**(1/12)) -1)##Calculo para saber o juros mensal
    mes=0 #esta variavel serve para contar os meses
    total=0 # armazenara o total de juros de todo o emprestimo
    print("MES\t JUROS   \t AMORTIZAÇÂO\t PARCELA\t VALOR RESTANTE")
    if escolha=="1":
        amor=valor/prazo
        mes=0
        for t in range(prazo):#ira repetir de acordo com o numero de prestações a serem pagas
            mes=mes+1# aumenta mais um mes no contador
            juros=(prazo-(t+1)+1)*amor*taxa#formula do juros
            valor=valor-(amor+juros)#subtrai o valor que ainda falta pagar pelo valor pago naquele mes
            total+=juros # o juros pago vai para o contador para futuramente mostrar o tatal de juros pago
            print(" \n")
            parcela= amor+juros#formula da parcela
            print ("%d >>\t %0.2f   \t %0.2f \t %0.2f \t %0.2f" %(mes , juros , amor , parcela , valor))#mostrará os valores com apenas 2 casas decimais
        print("\n \t \t  O JUROS TOTAL É >> %0.2f"%(total))

            
    if escolha=="2":
        parcela= (valor*taxa)/(1-(1+taxa)**(-prazo))#formula da parcela
        for t in range(prazo):
            juros=valor*taxa# formula do juros
            amor=parcela-juros#formula do amortizador
            mes=mes+1
            valor=(valor-parcela)+juros
            total+=juros
            print(" \n")
            print ("%d >>\t %0.2f   \t %0.2f \t %0.2f \t %0.2f" %(mes , juros , amor , parcela , valor))
        print("\n \t \t  O JUROS TOTAL É >> %0.2f"%(total))
            
            
    sair=input("\n \t Deseja fazer outra operação?\n SIM(1) ou NÃO(2)")# decisao se para ou continua no programa
    if sair=="2":break

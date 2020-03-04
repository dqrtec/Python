from datetime import datetime


def pedirValorNovamente(entrada):
    if(float(entrada) < 1):
        entrada = float(input("\nValor inválido para o campo. Digite o valor novamente :"))
        return float( pedirValorNovamente(entrada) )
    return float(entrada)

def pedirValorNovamenteInteiro(entrada):
    if(int(entrada) < 1):
        entrada = int(input("\nValor inválido para o campo. Digite o valor novamente :"))
        return int( pedirValorNovamente(entrada) )
    return int(entrada)

def verificaSe1ou2(entrada):
    if( (int(entrada) == 1) or (int(entrada)==2) ):
        return int(entrada)
    else:
        entrada = int(input("\nOs valores válidos para esse campo são 1 e 2 apenas\nDigite o valor novamente :"))
        return int( verificaSe1ou2(entrada) )

def imprimirValores(mesAtual ,saldoInicial, parcelaDoMes , amortizacao , juros , saldoFinal):
    print ("%d->\t %0.2f   \t %0.2f \t %0.2f \t %0.2f\t %0.2f" %(mesAtual ,saldoInicial, parcelaDoMes , amortizacao , juros , abs(saldoFinal) ) )

def imprimiJurosTotaisPago(jurosTotaisPago):
    print("\n \t \t  \033[93m Os JUROS Pagos Totalizam : %0.2f \033[0m"%(jurosTotaisPago))

def entradaValores():
    valor = float( input("Digite o valor do emprestimo : ") )
    valor = pedirValorNovamente(valor)

    prazoMeses = int( input("Digite a quantidade de meses : ") )
    prazoMeses = pedirValorNovamenteInteiro(prazoMeses)

    taxaJurosAnuais = float( input("Digite o juros anual(%a.a) : ") )
    taxaJurosAnuais = pedirValorNovamente(taxaJurosAnuais)
    
    formaPagamento = int( input("Qual tidpo de financiamento você deseja?\n\t 1 -> SAC \n\t 2 -> PRICE \n\t: ") )
    formaPagamento = verificaSe1ou2(formaPagamento)

    taxaJurosMensais= (((1+(taxaJurosAnuais/100))**(1/12)) -1)
    print("")
    return valor,prazoMeses,taxaJurosMensais,formaPagamento

def imprimeSac(valor,prazoMeses,taxaJurosMensais,formaPagamento):
    
    now = datetime.now()
    texto ="Sac"+ str(now.year)+"_"+ str(now.month)+"_"+ str(now.day)+"_"+ str(now.hour)+":"+ str(now.minute) + ".xlsx"
    relatorioSimulacao=open(texto,'w')

    relatorioSimulacao.write("MES\tSaldoInicial\tPARCELA\tAMORTIZAÇÂO\tJUROS\tVALOR RESTANTE")
    saldoInicial = valor
    jurosTotaisPago = 0
    amortizacao = valor/prazoMeses
    for mesAtual in range(1,prazoMeses+1):
        juros = (prazoMeses-mesAtual+1) * taxaJurosMensais * amortizacao 
        saldoFinal = saldoInicial - amortizacao
        parcelaDoMes = amortizacao+juros
        jurosTotaisPago += juros
        relatorioSimulacao.write("%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\n" %(mesAtual ,saldoInicial, parcelaDoMes , amortizacao , juros , abs(saldoFinal) ) )
        imprimirValores(mesAtual ,saldoInicial, parcelaDoMes , amortizacao , juros , saldoFinal)
        saldoInicial = saldoFinal
    relatorioSimulacao.close()
    imprimiJurosTotaisPago(jurosTotaisPago)

def imprimePRICE(valor,prazoMeses,taxaJurosMensais,formaPagamento):
    
    now = datetime.now()
    texto ="Price"+ str(now.year)+"_"+ str(now.month)+"_"+ str(now.day)+"_"+ str(now.hour)+":"+ str(now.minute) + ".xlsx"
    relatorioSimulacao=open(texto,'w')

    relatorioSimulacao.write("MES\tSaldoInicial\tPARCELA\tAMORTIZAÇÂO\tJUROS\tVALOR RESTANTE")
    jurosTotaisPago = 0 
    parcelaDoMes = (valor*taxaJurosMensais)/(1-(1+taxaJurosMensais)**(-prazoMeses))
    saldoInicial = valor
    for mesAtual in range(1,prazoMeses+1):
        juros = saldoInicial * taxaJurosMensais
        jurosTotaisPago += juros
        amortizacao = parcelaDoMes - juros
        saldoFinal = saldoInicial + juros - parcelaDoMes
        relatorioSimulacao.write("%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\n" %(mesAtual ,saldoInicial, parcelaDoMes , amortizacao , juros , abs(saldoFinal) ) )
        imprimirValores(mesAtual ,saldoInicial, parcelaDoMes , amortizacao , juros , saldoFinal)
        saldoInicial = saldoFinal
    relatorioSimulacao.close()
    imprimiJurosTotaisPago(jurosTotaisPago)

def escreveTabelaTela(valor,prazoMeses,taxaJurosMensais,formaPagamento):
    print("MES\t Saldo Inicial\t PARCELA  \t AMORTIZAÇÂO \t JUROS \t VALOR RESTANTE")
    if formaPagamento == 1:
        imprimeSac(valor,prazoMeses,taxaJurosMensais,formaPagamento)
    if formaPagamento == 2:
        imprimePRICE(valor,prazoMeses,taxaJurosMensais,formaPagamento)

while True:
    valor,prazoMeses,taxaJurosMensais,formaPagamento = entradaValores()
    escreveTabelaTela(valor,prazoMeses,taxaJurosMensais,formaPagamento)

    condicaoSaida = input("\n \t Deseja fazer outra operação?\n \tSIM(1) ou NÃO(2)")
    condicaoSaida = verificaSe1ou2(condicaoSaida)
    if condicaoSaida == 2:
        break
saldo=100000
prazo=12
j=12
taxa= (((1+(j/100))**(1/12)) -1)
mes=0
total=0
saldo_inicial=saldo
prestacao= (saldo*taxa)/(1-(1+taxa)**(-prazo))
print("MES\t SALDO  \t PRESTAÇÃO \t amortizacao\tJUROS \t saldo Final")
for t in range(prazo):
    juros=saldo*taxa
    amortizacao=prestacao-juros
    mes=mes+1
    saldo=(saldo-prestacao)+juros
    total+=juros
    print(" \n")
    saldo_inicial=saldo+amortizacao
    print ("%d >>\t %0.2f   \t %0.2f \t %0.2f \t %0.2f  \t %0.2f " %(mes,saldo_inicial , prestacao, amortizacao, juros , saldo  ))
print("\n \t \t  O JUROS TOTAL É >> \x1b[6;30;42m  %0.2f  \x1b[0m "%(total))
x=input(" ")
 

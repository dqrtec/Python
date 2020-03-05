saldo=100000  
prazo=12      
j=12          
taxa= (((1+(j/100))**(1/12)) -1)
mes=0 
total=0 
print("MES\t SALDO  \t PRESTAÇÃO \t amortizacaoTIZAÇÂO\tJUROS \t saldo Final")
amortizacao=saldo/prazo
mes=0
saldo_final=saldo
juros=0
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
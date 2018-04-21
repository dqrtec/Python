valor=[4.0,4.5,5.0,2.0,1.5]
cod , qtd = input().split(' ')
cod = int(cod)
qtd = int(qtd)
print("Total: R$ %0.2f"%(valor[cod-1]*qtd))

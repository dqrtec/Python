saldo = float(input("Digite seu saldo médio "))

if saldo > 400:

    credito = saldo*0.3

elif saldo > 300:

    credito = saldo*0.25

elif saldo >= 200:

    credito = saldo*0.2

else:

    credito = saldo*0.1

print ("SALDO = ", saldo, "CRÉDITO ESPECIAL = ", credito)
    

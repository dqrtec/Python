saldo_medio = float(input('Digite seu saldo médio do último ano\n'))
if saldo_medio > 400:
    credito = saldo_medio*0.3
elif saldo_medio >= 300:
    credito = saldo_medio*0.25
elif saldo_medio >= 200:
    credito = saldo_medio*0.2
else:
    credito = saldo_medio*0.1

print ('SALDO MEDIO:', saldo_medio, '\nCRÉDITO ESPECIAL:', credito)
    

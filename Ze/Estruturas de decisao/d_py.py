preco = float(input("digite o valor do produto "))
	
if preco<50:
    n_preco=preco*1.05
elif 100 > preco>=50:
    n_preco=preco*1.1
else:
    n_preco=preco*1.15
	
if n_preco<=80:
    categoria="D"
elif 80<n_preco<=120:
    categoria="C"
elif 120< n_preco<=200:
    categoria="B"
else: categoria="A"
	
print("o novo preco do produto é",n_preco," e a sua categoria é ", categoria)

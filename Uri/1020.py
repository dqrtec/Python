dias = int(input())

anos = dias // 365
dias -= anos*365

meses = dias //30
dias -= meses*30
	
print("%i ano(s)\n%i mes(es)\n%i dia(s)"%(anos , meses , dias))

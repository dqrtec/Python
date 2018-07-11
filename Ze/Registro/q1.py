pesquisa=[
{"sal":12000,"idade":15,"sexo":"m","filhos":1},
{"sal":11000,"idade":16,"sexo":"m","filhos":1},
{"sal":1000,"idade":17,"sexo":"m","filhos":2},
{"sal":10,"idade":18,"sexo":"m","filhos":3},
{"sal":100,"idade":1,"sexo":"m","filhos":2},
{"sal":1,"idade":12,"sexo":"m","filhos":1},
{"sal":500,"idade":13,"sexo":"m","filhos":1},
{"sal":10,"idade":14,"sexo":"m","filhos":1},
{"sal":10,"idade":1,"sexo":"m","filhos":2},
{"sal":10,"idade":2,"sexo":"m","filhos":3},
{"sal":10,"idade":3,"sexo":"m","filhos":1},
{"sal":10,"idade":4,"sexo":"m","filhos":1},
{"sal":10,"idade":5,"sexo":"m","filhos":1},
{"sal":10,"idade":6,"sexo":"m","filhos":1},
{"sal":10,"idade":7,"sexo":"m","filhos":1},
{"sal":13,"idade":8,"sexo":"m","filhos":1},
{"sal":12,"idade":9,"sexo":"m","filhos":1},
{"sal":11,"idade":10,"sexo":"m","filhos":2},
{"sal":11,"idade":15,"sexo":"m","filhos":1},
{"sal":15,"idade":15,"sexo":"m","filhos":2},
]

media_salario=0
media_filhos=0
maior_salario=0
total_mulheres=0
mulheres_ricas=0

for i in range(len(pesquisa)):
	media_salario+=pesquisa[i]["sal"]
	media_filhos+=pesquisa[i]["filhos"]

	if pesquisa[i]["sal"]>maior_salario:
		maior_salario=pesquisa[i]["sal"]

	if pesquisa[i]["sexo"] =="m":
		total_mulheres+=1
		if pesquisa[i]["sal"] > 10000:
			mulheres_ricas+=1


print(len(pesquisa))
print("media salarial:",media_salario/len(pesquisa))
print("media filhos:",media_filhos/len(pesquisa))
print("maior salario",maior_salario)
print("% de mulheres rica sao:",((mulheres_ricas/total_mulheres)*100) )
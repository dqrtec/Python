'''OS, data, valor,descrição do serviço realizado e nome do cliente.

a) a média dos valores dos serviços realizados
b) o nome do cliente que realizou o serviço mais caro, juntamente com a descriçãodesse serviço e a data de sua realização.'''

ofc=[
{"id":1,"data":"25/05/2017","valor":100,"descricao":"limpeza1","nome":"zezinho"},
{"id":2,"data":"25/05/2017","valor":200,"descricao":"limpeza2","nome":"zezinho"},
{"id":3,"data":"25/07/2017","valor":300,"descricao":"limpeza3","nome":"zezinho"},
{"id":4,"data":"25/08/2017","valor":400,"descricao":"limpeza4","nome":"zezinho"},
{"id":5,"data":"25/09/2017","valor":500,"descricao":"limpeza5","nome":"zezinho"},
{"id":6,"data":"25/01/2017","valor":600,"descricao":"limpeza6","nome":"zezinho"},
{"id":7,"data":"25/02/2017","valor":600,"descricao":"limpeza7","nome":"zezinho"},
{"id":8,"data":"25/03/2017","valor":800,"descricao":"limpeza8","nome":"zezinho"},
{"id":9,"data":"25/03/2017","valor":900,"descricao":"limpeza9","nome":"zezinho"},
{"id":10,"data":"05/04/2017","valor":100,"descricao":"limpeza1s","nome":"zezinho"},
{"id":11,"data":"05/05/2017","valor":200,"descricao":"limpeza1e","nome":"zezinho"},
{"id":12,"data":"05/06/2017","valor":300,"descricao":"limpeza1t","nome":"zezinho"},
{"id":13,"data":"05/07/2017","valor":400,"descricao":"limpeza1y","nome":"zezinho"},
{"id":14,"data":"05/08/2017","valor":500,"descricao":"limpeza1g","nome":"zezinho"},
{"id":15,"data":"20/09/2017","valor":600,"descricao":"limpeza1c","nome":"zezinho"},
{"id":16,"data":"20/10/2017","valor":700,"descricao":"limpeza1a","nome":"zezinho"},
{"id":17,"data":"20/10/2017","valor":800,"descricao":"limpeza1s","nome":"zezinho"},
{"id":18,"data":"20/10/2017","valor":900,"descricao":"limpeza1f","nome":"zezinho"},
{"id":19,"data":"20/10/2017","valor":1000,"descricao":"limpeza1h","nome":"zezinho"},
{"id":10,"data":"15/10/2017","valor":500,"descricao":"limpeza1k","nome":"zezinho"},
]

md=0
maior=0
indice=0
for i in range(len(ofc)):
	md+= ofc[i]["valor"]

	if ofc[i]["valor"]>maior:
		maior=ofc[i]["valor"]
		indice=i

print("media dos valores:",md/len(ofc))
print("nome:",ofc[indice]["nome"]," descrição:",ofc[indice]["descricao"]," data:",ofc[indice]["data"])
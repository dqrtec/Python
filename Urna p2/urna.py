def salvar_binario(dados):
	with open("dados_urna",'a') as arquivo:
		for dado in dados:
			aux = bytearray(str(dado))
			arquivo.write(aux)
			arquivo.write(",")
		arquivo.write("\n")

def cadastro_manual():
	cod = raw_input("\n\nQual o CODIGO do candidato? ")
	nome = raw_input("\n\nQual o NOME do candidato? ")
	cargo = raw_input("\n\nQual o CARGO do candidato? ")
	regiao = raw_input("\n\nQual a REGIAO dos votos? ")
	votos = raw_input("\n\nQuantos VOTOS tem o candidato? ")
	dados = [ cod, nome, cargo, regiao, votos]
	salvar_binario(dados)

def importar_csv():
	nome_arquivo = raw_input("\n\nQual no nome do arquivo csv? ")
	with open(nome_arquivo,"r") as arquivo:
		for linha in arquivo:
			if linha[-1] == '\n':
				linha = linha[:-1]
			if linha[-1] == ',':
				linha = linha[:-1]
			salvar_binario(linha.split(","))

def escolha_menu_principal():
	escolha = raw_input("\t--------Menu--------\n\t1 - Cadastrar Dados\n\t2 - Estatisticas dos Dados\n\t3 - Sair\nQual operacaodeseja fazer? ")
	return int(escolha)

def escolha_menu_cadastro():
	escolha = int(raw_input("\n\n\t--------Modo de Cadastro--------\n\t1 - Cadastro Manual\n\t2 - Importar CSV\n\t3 - Sair\nComo deseja cadastrar os dados? "))
	while escolha in dicionario_menu_cadastrar:
		dicionario_menu_cadastrar[escolha]()
		escolha = int(raw_input("\n\n\t--------Modo de Cadastro--------\n\t1 - Cadastro Manual\n\t2 - Importar CSV\n\t3 - Sair\nComo deseja cadastrar os dados? "))

def escolha_menu_estatisticas():
	dados = ler_dados()
	escolha = int(raw_input("\n\n\t--------Dados Estatisticos--------\n\t1 - Listar Todos Candidatos\n\t2 - Votos do Candidato\n\t3 - Votos do Candidato por regiao\n\t4 - Votos por regiao\n\t5 - Votos do candidato em cada regiao\n\t6 - Sair\nQuais estatisticas deseja saber? "))
	while escolha in dicionario_menu_estatisticas:
		dicionario_menu_estatisticas[escolha](dados)
		escolha = int(raw_input("\n\n\t--------Dados Estatisticos--------\n\t1 - Listar Todos Candidatos\n\t2 - Votos do Candidato\n\t3 - Votos do Candidato por regiao\n\t4 - Votos por regiao\n\t5 - Votos do candidato em cada regiao\n\t6 - Sair\nQuais estatisticas deseja saber? "))

def ler_dados():
	lista_dados = []
	with open("dados_urna",'r') as arquivo:
		for linha in arquivo:
			cod, nome, cargo, regiao, votos, _ = linha.split(',')
			dados = [cod, nome, cargo, regiao, votos]
			lista_dados.append(dados)
	return lista_dados

def todos_candidatos(dados):
	dicionario_candidados = {}
	for dado in dados:
		if dado[0] not in dicionario_candidados:
			dicionario_candidados[dado[0]] = dado[1]
	relatorio(dicionario_candidados)

def votos_por_candidato(dados):
	dicionario_candidados = {}
	for dado in dados:
		if (dado[0],dado[1]) not in dicionario_candidados:
			dicionario_candidados[(dado[0],dado[1])] = int(dado[4])
		else:
			dicionario_candidados[(dado[0],dado[1])] = int(dado[4]) + int(dicionario_candidados[(dado[0],dado[1])])
	relatorio(dicionario_candidados)

def votos_por_candidato_regiao(dados):
	dicionario_candidados = {}
	for dado in dados:
		if (dado[0],dado[1],dado[3]) not in dicionario_candidados:
			dicionario_candidados[(dado[0],dado[1],dado[3])] = int(dado[4])
		else:
			dicionario_candidados[(dado[0],dado[1],dado[3])] = int(dado[4]) + int(dicionario_candidados[(dado[0],dado[1],dado[3])])
	relatorio(dicionario_candidados)

def votos_por_regiao(dados):
	dicionario_regiao = {}
	for dado in dados:
		if (dado[3]) not in dicionario_regiao:
			dicionario_regiao[(dado[3])] = int(dado[4])
		else:
			dicionario_regiao[(dado[3])] = int(dado[4]) + int(dicionario_regiao[(dado[3])])
	relatorio(dicionario_regiao)

def votos_candidato_regiao(dados):
	cod_candidato = int(raw_input("Digite o codigo do candidato: "))
	dicionario_regiao = {}
	for dado in dados:
		if int(dado[0]) == cod_candidato:
			if (dado[3]) not in dicionario_regiao:
				dicionario_regiao[(dado[3])] = int(dado[4])
			else:
				dicionario_regiao[(dado[3])] = int(dado[4]) + int(dicionario_regiao[(dado[3])])
	relatorio(dicionario_regiao)

def relatorio(dicionario):
	print("\n\n\n=======RELARIO=======")
	print "atributos  -> valores"
	for chave in dicionario:
		print chave , "  -> ",dicionario[chave]

def __main__():
	operacao = escolha_menu_principal()
	while operacao in dicionario_menu_principal:
		dicionario_menu_principal[operacao]()
		operacao = escolha_menu_principal()

dicionario_menu_principal = {1:escolha_menu_cadastro, 2:escolha_menu_estatisticas}
dicionario_menu_cadastrar = {1:cadastro_manual, 2:importar_csv}
dicionario_menu_estatisticas = {1:todos_candidatos, 2:votos_por_candidato, 3:votos_por_candidato_regiao, 4:votos_por_regiao, 5:votos_candidato_regiao}
__main__()
def colocar_numero(tabuleiro,i,j,numero):
	tabuleiro[i][j] = [numero]
	return tabuleiro

def show_tabuleiro(tabuleiro):
	for i in range(9):
		for j in range(9):
			numero = tabuleiro[i][j][0] if tabuleiro[i][j] != [] else "_"
			print("{0}".format( numero ), end=" ")
			if j in [2,5]:
				print(" | ", end="")
		if i in [2,5]:
			print()
			print("=======================", end="")
		print()

def realizar_movimento(tabuleiro):
	tabuleiro_possibilidades = [[[] for j in range(9)] for i in range(9)]
	for i in range(9):
		for j in range(9):
			if len(tabuleiro[i][j]) == 0:
				numeros_horizontal = [tabuleiro[i][jj][0] for jj in range(9) if tabuleiro[i][jj] != []]
				numeros_vertical = [tabuleiro[ii][j][0] for ii in range(9) if tabuleiro[ii][j] != []]
				possibilidades = set()
				possibilidades.union(numeros_horizontal)
				possibilidades.union(numeros_vertical)
				todos_numeros = set([i for i in range(1,10)])
				possibilidades = todos_numeros - possibilidades
				if len(possibilidades) == 1:
					tabuleiro_possibilidades[i][j] = [possibilidades.pop()]
				else:
					tabuleiro_possibilidades[i][j] = []
			else:
				tabuleiro_possibilidades[i][j] = [tabuleiro[i][j][0]]
	return tabuleiro_possibilidades

tabuleiro = [[[] for j in range(9)] for i in range(9)]

# tabulerio = colocar_numero(tabuleiro,0,1,6)
# tabulerio = colocar_numero(tabuleiro,0,2,5)
# tabulerio = colocar_numero(tabuleiro,0,6,2)

# tabulerio = colocar_numero(tabuleiro,1,0,8)
# tabulerio = colocar_numero(tabuleiro,1,5,4)
# tabulerio = colocar_numero(tabuleiro,1,7,7)

# tabulerio = colocar_numero(tabuleiro,2,0,9)
# tabulerio = colocar_numero(tabuleiro,2,4,3)
# tabulerio = colocar_numero(tabuleiro,2,8,1)

# #############################################

# tabulerio = colocar_numero(tabuleiro,3,3,9)
# tabulerio = colocar_numero(tabuleiro,3,7,4)

# tabulerio = colocar_numero(tabuleiro,4,2,3)
# tabulerio = colocar_numero(tabuleiro,4,6,5)

# tabulerio = colocar_numero(tabuleiro,5,1,1)
# tabulerio = colocar_numero(tabuleiro,5,5,8)

# #############################################

# tabulerio = colocar_numero(tabuleiro,6,0,1)
# tabulerio = colocar_numero(tabuleiro,6,4,5)
# tabulerio = colocar_numero(tabuleiro,6,8,6)

# tabulerio = colocar_numero(tabuleiro,7,1,4)
# tabulerio = colocar_numero(tabuleiro,7,3,7)
# tabulerio = colocar_numero(tabuleiro,7,8,2)

# tabulerio = colocar_numero(tabuleiro,8,2,8)
# tabulerio = colocar_numero(tabuleiro,8,6,9)
# tabulerio = colocar_numero(tabuleiro,8,7,5)

show_tabuleiro(tabuleiro)

tabuleiro = realizar_movimento(tabuleiro)

print()
show_tabuleiro(tabuleiro)
def soma_pares():
        soma=0
        numeros_pares=[]
        verificador_limites = True

        while verificador_limites:
                limite_inferior = int(input("Digite o limite inferior "))
                limite_superior = int(input("Digite o limite superior "))
                if limite_inferior < limite_superior:
                        verificador_limites = False
                else:
                        print("O limite inferior é maior que o limite superior")
                
        for i in range(limite_inferior+1 , limite_superior):
                if i % 2 ==0:
                        numeros_pares.append(i)
                        
        for j in range(0,len(numeros_pares)):
                soma=soma+numeros_pares[j]

        print("lista de numeros pares encontrados no intervalo ",numeros_pares)
        return soma
	
	
	
        
print("Soma dos numeros da lista: ",soma_pares())

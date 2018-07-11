contas={}
valida_banco=True
for i in range(3):
    numero_conta=int(input("Digite o numero da %dº conta"%(i+1)))
    contas[numero_conta]=0
    
while valida_banco:
    
    menu=int(input("----menu----\n____________________\n| 1 -> Credito |\n 2-> Debito   |\n| 3 -> Transferir  |\n| 4 -> Saldo  |\n| 0 -> Sair   |\n|_________________|"))
        
    if menu==1:
        
        valida_conta=True
        while valida_conta:
            numero_conta=int(input("Digite o numero da conta"))
            valida_credito=True
            if numero_conta in contas:
                while valida_credito:
                    credito=float(input("Digite o valor a ser acrescido a conta"))
                    if credito<0:
                        print("entrada invalida")
                    else:
                        valida_credito=False
                        contas[numero_conta]+=credito
                valida_conta=False
            else:
                print("conta nao encontrada!")
                
    elif menu==2:
        
        valida_conta=True
        while valida_conta:
            numero_conta=int(input("Digite o numero da conta"))
            valida_credito=True
            if numero_conta in contas:
                while valida_credito:
                    credito=float(input("Digite o valor a ser acrescido a conta"))
                    if credito<0:
                        print("entrada invalida")
                    else:
                        valida_credito=False
                        contas[numero_conta]-=credito
                valida_conta=False
            else:
                print("conta nao encontrada!")
                
    elif menu==3:
        
        valida_conta1=True
        while valida_conta1:
            numero_conta1=int(input("Digite o numero da conta de origem "))
            if numero_conta1 in contas:
                valida_conta1=False
            else:
                print("conta nao encontrada!")


        valida_conta=True
        while valida_conta:
            numero_conta=int(input("Digite o numero da conta"))
            if numero_conta in contas:
                valida_conta=False
            else:
                print("conta nao encontrada!")


        valida_valor=True
        while valida_valor:
            valor=float(input("Digite o valor a ser transferido "))
            if valor>contas[numero_conta1] or valor<0:
                print("valor a ser transferido é invalido")
            else:
                valida_valor=False
        
        contas[numero_conta1]-=valor
        contas[numero_conta]+=valor

                
    elif menu==4:
        
        valida_conta=True
        while valida_conta:
            numero_conta=int(input("Digite o numero da conta"))
            if numero_conta in contas:
                print(numero_conta,", saldo de?",contas[numero_conta])
                valida_conta=False
            else:
                print("conta nao encontrada!")
                
    elif menu==0:
       valida_banco=False
    else:
        print("entrada invalida!")
    


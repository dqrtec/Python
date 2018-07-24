def conta_energia():
    tabela_de_valores=[[0,0],[0.40 , 0.65],[0.55 , 0.60],[0.55 , 0.60]]
    continuar = True
    validar_kwh = True
    validar_tipo = True

    while validar_kwh:
        consumo_kwh = input("Digite seu consumo de energia em KWH ")
        if consumo_kwh=="" :
            print("consumo invalido:Valor do consumo nao foi digitado ")
        elif float(consumo_kwh)<0 :
            print("consumo invalido:Valor do consumo é menor que 0 ")
        else:
            validar_kwh=False
            consumo_kwh = float(consumo_kwh)

    while validar_tipo:
        tipo_consumidor=input("Insira o seu tipo de consumidor\n 1 para Residencial\n 2 para Industrial\n 3 para Comercial\n")
        if "1"!=tipo_consumidor and tipo_consumidor!="2" and tipo_consumidor!="3":
            print("Entrada invalida!")
        else:
            validar_tipo = False
            tipo_consumidor=int(tipo_consumidor)

        
    valor_pagar=0
    indice_valor=0
    if tipo_consumidor == 1:
        if consumo_kwh<=500:
            valor_pagar = consumo_kwh * tabela_de_valores[tipo_consumidor][0]
            indice_valor=0
        else:
            valor_pagar = consumo_kwh * tabela_de_valores[tipo_consumidor][1]
            indice_valor=1
            
    elif tipo_consumidor == 2:
        if consumo_kwh<=5000:
            valor_pagar = consumo_kwh * tabela_de_valores[tipo_consumidor][0]
            indice_valor=0
        else:
            valor_pagar = consumo_kwh * tabela_de_valores[tipo_consumidor][1]
            indice_valor=1

    else:
        if consumo_kwh<=1000:
            valor_pagar = consumo_kwh * tabela_de_valores[tipo_consumidor][0]
            indice_valor=0
        else:
            valor_pagar = consumo_kwh * tabela_de_valores[tipo_consumidor][1]
            indice_valor=1
            
    print("\nValor do KWH:",tabela_de_valores[tipo_consumidor][indice_valor])
    print("Consumo de KWH:",consumo_kwh)
    return(valor_pagar)


print("Valor a ser pago = ",conta_energia())

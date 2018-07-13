idade=int(input("Digite a sua idade "))
peso=float(input("Digite o seu peso "))
if idade<20 :
    if peso<60:
        risco= 9
        print("O seu risco é " , risco)
    elif peso>90:
        risco= 7
        print( "O seu risco é " , risco)
    else:
        risco= 8
        print( "O seu risco é " , risco)
elif idade>50 :
    if peso<60:
        risco= 3
        print( "O seu risco é " , risco)
    elif peso>90:
        risco= 1
        print("O seu risco é " , risco)
    else:
        risco= 2
        print("O seu risco é " , risco)
else:
    if peso<60:
        risco= 6
        print("O seu risco é " , risco)
    elif peso>90:
        risco= 4
        print(  "O seu risco é " , risco)
    else:
        risco= 5
        print( "O seu risco é " , risco)

data=input("Digite uma data ")
x=False
y=False
data=data.split("/")

if 0<int(data[0])<=31:
    if 0<int(data[1])<=12:
        y=True



if 0<int(data[0])<=12:
    if 0<int(data[1])<=31:
        x=True


if x and y:
    print("indeterminavel")
elif x:
    print("americano")
elif y:
    print("brasileiro")
else:
    print("INVALIDO")

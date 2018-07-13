b=[]
for i in range(0, 100):
    b.append(int(input("Digite um numero ")))
somatorio=0
for i in range(0,50):
    somatorio= somatorio+ ((b[i] - b[99-i])**3)
print("somatório: " , somatorio)

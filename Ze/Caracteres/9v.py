email="daiel@avanz.com"
arroba=False
com=True#False
for i in range(len(email)-1):
    if email[i]=="@":
        arroba=True
##if email[len(email)-1-3:]==".com":
##    com=True

if arroba and com:
    print("E-mail VALIDO")
elif arroba:
    print("NAO apresenta o @")
elif com:
    print("NAO apresenta o .com")
else:
    print("E-mail INVALIDO!!!!")


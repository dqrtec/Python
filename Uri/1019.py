segundo = int(input())

horas = segundo //3600
segundo -= 3600*horas

minutos = segundo //60
segundo -= 60*minutos

print("%i:%i:%i"%(horas,minutos , segundo))

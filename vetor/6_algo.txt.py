algoritmo
declare lista[1000] numerico
		divisor , fat , somatorio , c , i , j , cont numerico
divisor<-3
fat <- 1
somatorio <- 0
cont<-1
x <- (leia x*pi)/180
lista.[cont]<-x
somatorio<-somatorio+x

para i <-1 ate 15 faça
inicio
    para j <-1 ate divisor+1
		inicio
			fat <- fat*j
		fim
        
    se mod(i/2)==0
    entao	inicio 
			somatorio<-(somatorio+(x**divisor)/fat)
			lista[j]<-(x**divisor)/fat)
			fim
    senao
        somatorio<- somatorio - ((x**divisor)/fat)
        lista[j]<- -1*((x**divisor)/fat))
    
    divisor<-divisor+2
    fat<-1
escreva somatorio
escreva lista
fim_algoritmo
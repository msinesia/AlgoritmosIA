#neuronio mcCulloch e Pitts b�sico
#entradas - valores aleat�rios
x1 <- 2
x2 <- 3
x3 <- -4
x4 <- 0

#pesos - valores aleat�rios
p1 <- 1
p2 <- 3
p3 <- 1
p4 <- -1

#threshold - limiar
bias <- 1.5

#somat�rio - neur�nio
no1 <- sum (x1*p1,x2*p2,x3*p3,x4*p4)
no1

#fun��o de ativa��o beeeem b�sica
if (no1 >= bias) {
  y <- 1
  #print(no1)
  
} else {
  y <- 0
  #print(no1)
}


# JOC DE PROVES
#Entrada       Sortida
#1,2            1,2
#2,1            1,2
#-3, -36        -36,-3
#2,2             2,2
numero1=int(input("indica primer numero:"))
numero2=int(input("indica segundo numero:"))
if (numero1==numero2):
    print("Son igual")
else:    
    if numero1<numero2:
       print( numero1, numero2,)

    else:
        print(numero2, numero1)

#coding:ut8

menu = [[1,"Super: Normal",1.5],[2,"Super: Turbo",1.55],[3,"Sin plomo: Normal",1.6],[4,"Sin plomo: Con Aditivos(sabor naranja)",1.65],[5,"Diesel: Normal",1.7],[6,"Diesel: Fast&Furius",1.75]]

print("Aqui tienes el menú:")
print("Super: Normal (", menu[0][2],"€)>>>>>>>> 1 ",    "--------Turbo(",menu [1][2],"€)>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2",sep="")
print("Sin plomo: Normal(",menu[2][2],"€)>>>>> 3",  "-----------Con aditivos(sabor naranja)(",menu[3][2],"€)>>>>> 4",sep="")
print("Diesel: Normal(",menu[4][2],"€)>>>>>>>>>5",    "---------Fast&Furius(",menu[5][2],"€)>>>>>>>>>>>>>>>>>>>>>>> 6 ",sep="")

gasolinera = int(input("Que tipo de gasolina quieres: "))
while ((gasolinera < 1 ) or (gasolinera > 6)):
    print("Error")
    gasolinera = int(input("Que tipo de gasolina desea: "))
if ((gasolinera>= 1) and (gasolinera <=6)):
    litros = float(input(" Indiqe cuantos litros quieres: "))
    while litros < 0.5:
        print("Error")
        litros = float(input("Indiqe cuantos litros quieres: "))
    if gasolinera == 1:
        print (" Usted ha escogido " , litros," litros de " , menu [0][1], " con un valor de ","{0:.3f}".format(litros* menu [0][2]),"€",sep="")
    if gas == 2:
        print (" Usted ha escogido " , litros," litros de " , menu[1][1], " con un valor de ","{0:.3f}".format(litros*  menu [1][2]),"€",sep="")
    if gas == 3:
        print (" Usted ha escogido " , litros," litros de " , menu [2][1], " con un valor de ","{0:.3f}".format(litros* menu [2][2]),"€",sep="")
    if gas == 4:
        print (" Usted ha escogido " , litros," litros de " , menu [3][1], " con un valor de ","{0:.3f}".format(litros* menu [3][2]),"€",sep="")
    if gas == 5:
        print (" Usted ha escogido " , litros," litros de " , menu [4][1], " con un valor de ","{0:.3f}".format(litros* menu [4][2]),"€",sep="")
    if gas == 6:
        print (" Usted ha escogido " , litros," litros de " , menu [5][1], " con un valor de ","{0:.3f}".format(litros* menu [5][2]),"€",sep="")

print('Total recaudado = %d' %total)

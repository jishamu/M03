#coding:utf8
anyo=int(input("Dime un año: "))
if (((anyo % 4 == 0) and (anyo % 100 != 0)) or (anyo % 400 == 0)):
    print(anyo, "es bisiesto.")
      
else:
    print(anyo, "no es bisiesto.")

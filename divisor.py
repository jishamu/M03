#coding:utf8
dividendo=int(input("Introduce un dividendo:"))
divisor=int(input("Introduce un divisor:"))
if ((dividendo==0) or (divisor==0)):
	print("No se puede")
else:
	if (dividendo % divisor):
		print("La división no es exacta. Cociente:", (dividendo // divisor), 
          "Resto:", (dividendo % divisor))
	else:
		print("La división es exacta. Cociente:",(dividendo // divisor))

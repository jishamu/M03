
#coding uft·8
loteria=input ("te ha tocado loteria:")
if (loteria=="si"):
  print("Puedes ganar 3000€ al mes")
	
casar=input("Te casas con un(a) millonati")
edad=int(input("Cuantos años tiene:"))
corazon=input("Tiene problema de corazón")
casado=input("Esta casado:")
if((casar=="si")and(edad>80)and(corazon=="si")and(casado=="si")):
  print("Puedes ganar 3000€ al mes")
	
estudiar=input("estudias:")
M01=int(input("Cuantos has sacado:"))
M02=int(input("Cuantos has sacado:"))
M03=int(input("Cuantos has sacado:"))
M05=int(input("Cuantos has sacado:"))
if((M01==9)and(M02==10)and(M03==8)and((M05==6)and(M05<=8))):
	print ("Puedes ganar 3000€ al mes")
ponderada=(M01**0.3)+(M02**0.4)+(M03**0.25)+(M05**0.05)
if (ponderada>=8):
  print("Puedes ganar 3000€ al mes")
else:
  print("No puedes puedes ganar 3000€ al mes")

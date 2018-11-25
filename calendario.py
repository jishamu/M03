#coding:utf8
print ("Enero")
for cal in range(0, 365):
	print ("Dia " , cal+1)
	if (cal % 365) == (31-1):
		print("Febrero")
	if (cal % 365) == (59-1):
		print("Marzo")
	if (cal % 365) == (90-1):
		print("abril")
	if (cal % 365) == (121-1):
		print("Mayo")
	if (cal % 365) == (151-1):
		print("Junio")
	if (cal % 365) == (182-1):
		print("Julio")
	if (cal % 365) == (213-1):
		print("Agusto")
	if (cal % 365) == (243-1):
		print("Septiembre")
	if (cal % 365) == (274-1):
		print("Octubre")
	if (cal % 365) == (304-1):
		print("Noviembre")
	if (cal % 365) == (334-1):
		print("Deciembre")
	

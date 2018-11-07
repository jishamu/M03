
anyo_actual=int(input("En que año estamos:"))
2	anyo_cualquiera=int(input("Dime cualquier año:"))
3	if (anyo_actual==anyo_cualquiera):
4	    print("Son el mismo año")
5	    
6	else:
7	    if (anyo_cualquiera>anyo_actual):
8	        resultado1=(anyo_cualquiera-anyo_actual)
9	        print("Para llegar al año", anyo_cualquiera, "falta", resultado1, "años")
10	    
11	    else:
12	        if (anyo_cualquiera<anyo_actual):
13	            resultado2=(anyo_actual-anyo_cualquiera)
14	        print("Desde el año", anyo_cualquiera, "han pasado", resultado2, "años")

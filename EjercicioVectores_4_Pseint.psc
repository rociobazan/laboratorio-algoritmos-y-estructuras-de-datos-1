Algoritmo sin_titulo
	Dimension Vector1[20]
	aux = 0
	//cargo el vector
	Para x<-1 Hasta 20 Con Paso 1 Hacer
		Vector1[x] = azar(100)
	Fin Para
	
	//muestro el vector desordenado
	Mostrar "Vector desordenado"
	Para x<-1 Hasta 20 Con Paso 1 Hacer
		Mostrar Vector1[x]
	Fin Para
	
	//Ordeno los elementos de forma ascendente
	
	Para x<-1 Hasta 20 Con Paso 1 Hacer
		Para i<-1 Hasta 19 Con Paso 1 Hacer
			Si vector1[i] > vector1[i+1] Entonces
				aux = vector1[i]
				vector1[i] = vector1[i+1]
				vector1[i+1] = aux
			FinSi
		Fin Para
		
		
	Fin Para
	
	//Muestro el vector ordenado
	Mostrar "El vector ordenado es"
	Para x<-1 Hasta 20 Con Paso 1 Hacer
		
		Mostrar vector1[x]
	Fin Para
	
	
FinAlgoritmo

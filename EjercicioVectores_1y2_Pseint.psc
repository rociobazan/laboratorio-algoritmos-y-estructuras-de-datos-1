Algoritmo EjerciciosVectores1
	Dimension cedula[10]
	Dimension nombre[10]
	Definir encontrado Como Logico
	encontrado = Falso
	
	Para x<-1 Hasta 10 Con Paso 1 Hacer
		Mostrar "Igrese el nombre del estudiante"
		leer nombre[x]
		Mostrar "Ingrece la c�dula del estudiante"
		leer cedula[x]
	Fin Para
	
	Para x<-1 Hasta 10 Con Paso 1 Hacer
		Mostrar "El nombre del alumno es " + nombre[x] + " y su c�dula es " + cedula[x]
	Fin Para
	
	Mostrar "Ingrese el n�mero de c�dula a buscar"
	Leer cedulaBuscada
	
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Si cedula[i] = cedulaBuscada Entonces
			Mostrar "Esa c�dula corresponde a " + nombre[i]
			encontrado = Verdadero
		FinSi
	Fin Para
	
	Si encontrado = Falso Entonces
		Mostrar "No encontramos ning�n estudiante con la c�dula ingresado"
	FinSi
	
	
	
	
FinAlgoritmo


	Algoritmo sin_titulo
		// �ndices
		j = 1
		z = 1
		Definir cant como Entero
		Mostrar "�Cu�ntos n�meros quiere ingresar?"
		Leer cant
		
		Dimension A[cant]
		Dimension B[cant] 
		Dimension C[cant] 
		
		// Carga del vector A
		Para x <- 1 Hasta cant Con Paso 1 Hacer
			Mostrar "Ingrese un n�mero"
			Leer A[x]
		Fin Para
		
		// Clasificar los n�meros
		Para i <- 1 Hasta cant Con Paso 1 Hacer
			Si (A[i] Mod 2 <> 0) Entonces
				B[j] = A[i]
				j = j + 1
			FinSi
			Si (A[i] Mod 3 == 0) Entonces
				C[z] = A[i]
				z = z + 1
			FinSi
		Fin Para
		
		// Imprimir vector A
		Mostrar "Vector A (todos los n�meros):"
		Para k <- 1 Hasta cant Con Paso 1 Hacer
			Mostrar A[k]
		Fin Para
		
		// Imprimir vector B (n�meros impares)
		Mostrar "Vector B (n�meros impares):"
		Para k <- 1 Hasta j - 1 Con Paso 1 Hacer
			Mostrar B[k]
		Fin Para
		
		// Imprimir  vector C (m�ltiplos de 3)
		Mostrar "Vector C (m�ltiplos de 3):"
		Para k <- 1 Hasta z - 1 Con Paso 1 Hacer
			Mostrar C[k]
		Fin Para

FinAlgoritmo

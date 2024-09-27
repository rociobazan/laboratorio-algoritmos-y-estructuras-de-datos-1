#1) Práctica Método Index() 1
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

palabra = "ordenador"
resultado = palabra[4]
print(resultado)

#2) Práctica Método Index() 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado = frase.find("práctica")

print(resultado)

#3) Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado = frase.rfind("práctica")

print(resultado)

#-----------------------------------------------------------------------------------------------------------

# Práctica Sub-Strings 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:

# "Controlar la complejidad es la esencia de la programación"

# Pista: "Controlar" tiene un largo de 9 caracteres.

frase = "Controlar la complejidad es la esencia de la programación"

fragmento = frase[0:9]
print(fragmento)

# Práctica Sub-Strings 2
# Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

fragmento = frase[9::3]

print(fragmento)

# Práctica Sub-Strings 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

print(frase[::-1])

#-----------------------------------------------------------------------------------------------------------

# Práctica Métodos de String 1
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:

texto = "Este es un texto"

print(texto.upper())

# Práctica Métodos de String 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]

print(" ".join(lista_palabras))

# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:

# "Si la implementación es difícil de explicar, puede que sea una mala idea."

# los siguientes pares de palabras:

# "difícil" --> "fácil"

# "mala" --> "buena"

# y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

frase_modificada = frase.replace("difícil", "fácil").replace("mala", "buena")

print(frase_modificada)

#--------
print("Código de Rocío Bazan")

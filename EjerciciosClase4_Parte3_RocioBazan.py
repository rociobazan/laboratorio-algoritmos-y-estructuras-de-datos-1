# # # # # Práctica Zip 1
# # # # # Muestra en pantalla frases como la del siguiente ejemplo:

# # # # # La capital de Alemania es Berlín

# # # # # Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.



capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


for pais, capital in zip (paises, capitales):
    print(f"La capital de {pais} es {capital}")


# # # # # Práctica Zip 2
# # # # # Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.

marcas = ["ford","chevrolet","lancia","audi","fiat","volkswagen","IKA"]
productos =["mustang","corvette","delta integrale","S4","125 bialbero","gol power","torino tsx"]

for marca, producto in zip (marcas, productos):
    mi_zip = marca, producto
    print(mi_zip)

# # # # # Práctica Zip 3
# # # # # Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

# # # # # uno / um / one

# # # # # dos / dois / two

# # # # # tres / três / three

# # # # # cuatro / quatro / four

# # # # # cinco / cinco / five

# # # # # El resultado deberá seguir la estructura:

# # # # # [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

numeros_espaniol = ['uno','dos','tres','cuatro','cinco'] 
numeros_portugues = ['um','dois','três',"quatro","five"]
numeros_ingles = ['one','two','three','four','five']

for numero_espaniol, numero_portugues, numero_ingles in zip (numeros_espaniol, numeros_portugues, numeros_ingles):
    numeros = numero_espaniol, numero_portugues, numero_ingles
    list(numeros)
    print(numeros)

# # # # # Práctica Min y Max 1
# # # # # Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)

# # # # Práctica Min y Max 2
# # # # Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

valor_maximo = max(lista_numeros)
valor_minimo = min(lista_numeros)
rango = valor_maximo - valor_minimo

print(rango)

# # # # Práctica Min y Max 3
# # # # Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

# # # # Almacena dicho valor en una variable llamada edad_minima.

# # # # También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())

print(edad_minima, ultimo_nombre)

# # # Práctica Random 1
# # # Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio


from random import randint
aleatorio = randint(1, 10)
print(aleatorio)

# # Práctica Random 2
# # Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio

from random import random
aleatorio = random()
print(aleatorio)

# Práctica Random 3
# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

from random import choice
sorteo = choice(nombres)
print(sorteo)

#---
print("Código de Rocío Bazán")
# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buenas chances"

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

from random import randint
def lanzar_dados():
    resultado1 = randint(1,6)
    resultado2 = randint(1,6)
    return resultado1, resultado2

valores = lanzar_dados()

def evaluar_jugada(valores):
    suma_dados = sum(valores)
    if suma_dados >= 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    return mensaje

resultado = evaluar_jugada(valores)
print(resultado)

# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promecdio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

lista_numeros = [1,2,15,7,2]
def reducir_lista(lista):
    lista = list(set(lista))
    lista.remove(max(lista))
    return lista

lista_reducida = reducir_lista(lista_numeros)

def promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio


# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
from random import choice

def lanzar_moneda():
    resultado = choice(["Cara", "Cruz"])
    return resultado

resultado_moneda = lanzar_moneda()
lista_numeros = [7, 5, 23, 13, 20, 84, 40]

def probar_suerte(moneda, lista):
    lista_vacia = []
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return lista_vacia
    else:
        print("La lista fue salvada")
        return lista

jugada = probar_suerte(resultado_moneda, lista_numeros)
print(jugada)

# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

def suma_cuadrados(*args):
    suma= 0
    for num in args:
        cuadrado = num ** 2
        suma = suma + cuadrado
    return suma

print(suma_cuadrados(1,2,4))

# Práctica sobre Argumentos Indefinidos (*args) 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    suma=0
    for num in args:
        suma = suma + abs(num)
    return suma


# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

# La función debe devolver el siguiente mensaje:

# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma = sum(args)
    return f"{nombre}, la suma de tus números es {suma}"

# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    return len(kwargs)

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    lista = list(kwargs.values())
    return lista

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:

# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# Mostrará en pantalla:

# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")


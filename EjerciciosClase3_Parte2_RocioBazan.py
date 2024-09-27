
# Práctica Listas 1
# Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista = ["Rojo", "Verde", "Amarillo", "Azul", "Rosa"]


# Práctica Listas 2
# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("Motocicleta")


# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.


# Práctica Listas 3
# Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.

# manzana

# banana

# mango

# cereza

# sandía

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

#-------------------------------------------------------------------

# Práctica Diccionarios 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:

# nombre: Karen

# apellido: Jurgens

# edad: 35

# ocupacion: Periodista

# Los nombres de las claves y valores deben ser iguales a la consigna.

mi_dic = {"Nombre":"Karen", "Apellido":"Jurgens", "Edad":"35", "Ocupación":"Periodista"}
print(mi_dic)

# Práctica Diccionarios 2
# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

# Práctica Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

# nombre: Karen

# apellido: Jurgens

# edad: 36

# ocupacion: Editora

# pais: Colombia

# para ello, no debes 
# cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

mi_dic = {"Nombre":"Karen", "Apellido":"Jurgens", "Edad":"35", "Ocupación":"Periodista"}
mi_dic["Edad"]=36
mi_dic["Ocupación"] = "Editora"
mi_dic["Pais"] = "Colombia"
print(mi_dic)

#---------------------------------------------------------------------

# # Práctica Tuples 1
# # Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

cantidad = mi_tupla.count(2)
print(cantidad)

# # Práctica Tuples 2
# # Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)

# # Práctica Tuples 3
# # Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)

a, b, c, d = mi_tupla

#-----
print("Código de Rocío Bazan")

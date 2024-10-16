
def validar_nombre(nombre): 
    nombre = nombre.strip() #le quita los espacios al principio y al fin
    if nombre.replace(" ", "").isalpha(): #quita los espacios del medio, verifica que sea alfabético
            return True #si cumple con todo devuelve verdadero, sino falso.
    return False

def contar_palabras(lista_nombres):
    for nombre in lista_nombres: #analizando cada nombre de la lista
        cantidad_palabras= len(nombre.split()) #lo separa en distintas unidades, dadas por el espacio entre las palabras que componen el nombre. Devuelve una lista con esas unidades.
        print(f"El nombre {nombre} tiene {cantidad_palabras} palabra/s")

def filtrar_por_inicial(lista_nombres, letra):
    nombres_inicial = []
    for nombre in lista_nombres:
        if nombre.lower().startswith(letra.lower()):
            nombres_inicial.append(nombre)
    if not nombres_inicial:
        return f"No hay nombres que inicien con la letra {letra}"
    else:
        return f"Los nombres que comienzan con {letra} son {', '.join(nombres_inicial)}"


def contar_vocales_consonantes(lista_nombres):
    cant_vocales=0
    cant_consonantes = 0
    vocales = "aeiouáéíóú"
    for nombre in lista_nombres:
        nombre = nombre.lower()
        for letra in nombre:
            if letra.isalpha():
                if letra in vocales:
                    cant_vocales += 1
                else:
                    cant_consonantes += 1
        
    return f"Hay {cant_vocales} vocales y {cant_consonantes} consonantes"

def buscar_nombre(nombre_buscado, lista_nombres):
    for nombre in lista_nombres:
            if nombre.lower() == nombre_buscado:
                return f"El nombre {nombre_buscado} si está en la lista"
    return f"El nombre {nombre_buscado} no está en la lista"

def contar_caracteres(lista_nombres):
    contador = 0
    lista_5_caracteres = []
    for nombre in lista_nombres:
        if len(nombre.replace(" ","")) > 5:
            contador = contador + 1
            lista_5_caracteres.append(nombre)
    return contador, lista_5_caracteres

def nombres_en_formato(formato, lista_nombres):
    if formato.lower() == "minuscula" or formato.lower() == "minúscula":
        return [nombre.lower() for nombre in lista_nombres]
    elif formato.lower() == "mayuscula" or formato.lower() == "mayúscula":
        return [nombre.upper() for nombre in lista_nombres]
    else:
        return lista_nombres

lista_nombres = []

while True:
    nombre = input("""Ingresa el nombre del estudiante. 
    Para terminar ingrese: FIN.
    Para ver los nombres ya registrados ingrese: REPETIR """)

    if nombre.upper() == "FIN": #Si lo ingresado es FIN termina el ciclo
        break
    elif nombre.upper() == "REPETIR": #si ingresa REPETIR me muestra la lista hasta el momento y luego sigue
        print(f"Los nombres ingresados son: {', '.join(lista_nombres)}")
        continue

    if validar_nombre(nombre):
        lista_nombres.append(nombre)
    else:
        print("Por favor, ingrese un nombre válido.")
    
while True:
    print("MENÚ DE OPCIONES")
    print("1.Mostrar nombres ingresados")
    print("2.Ordenar los nombres alfabéticamente")
    print("3.Mostrar el nombre más largo y el más corto")
    print("4.Contar vocales y consonantes")
    print("5.Contar palabras en cada nombre")
    print("6.Invertir cada nombre ingresado")
    print("7.Mostrar nombres que comienzan con una letra específica")
    print("8.Buscar si un nombre está en la lista")
    print("9.Contar cuántos nombres tienen más de 5 caracteres")
    print("10.Convertir los nombres a mayúsculas o minúsculas")
    print("11.Salir")

    opcion = int(input("Ingrese el número correspondiente a la opción deseada"))

    if opcion == 1:
        print(f"Los nombres ingresados son {', '.join(lista_nombres)}")
    elif opcion == 2:
        lista_nombres_alf =sorted(lista_nombres) #sorted crea otra lista con los datos de la original ordenada
        print(f"Nombres en orden alfabético: {', '.join(lista_nombres_alf)}")
    elif opcion == 3:
        nombre_corto = min(lista_nombres, key=len)
        nombre_largo = max(lista_nombres, key=len)
        print(f"El nombre más largo es {nombre_largo} y el más corto {nombre_corto}.")
    elif opcion == 4:
        print(contar_vocales_consonantes(lista_nombres))
    elif opcion == 5:
        contar_palabras(lista_nombres)
    elif opcion == 6:
        nombres_invertidos = [nombre[::-1] for nombre in lista_nombres]
        print(f"Los nombres invertidos son: {', '.join(nombres_invertidos)}")
    elif opcion == 7:
        letra = input("Ingrese la letra por la cuál quiere filtrar los nombres")
        print(filtrar_por_inicial(lista_nombres, letra))
    elif opcion == 8:
        nombre_buscado = input("Ingrese el nombre que quiere buscar").lower()
        print(buscar_nombre(nombre_buscado, lista_nombres))
    elif opcion == 9:
        cant_nombres, lista_5_caracteres = contar_caracteres(lista_nombres)
        print(f"Hay {cant_nombres} nombres con más de 5 caracteres. Ellos son {', '.join(lista_5_caracteres)}")
    elif opcion == 10:
        formato_elegido = input("¿Quiere ver los nombres en mayúsucula o en minúscula?")
        print(', '.join(nombres_en_formato(formato_elegido, lista_nombres)))
    elif opcion == 11:
        print("Programa terminado")
        break
    else:
        print("Ingrese una opción válida")

       
    
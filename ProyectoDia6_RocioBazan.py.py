from pathlib import Path
import shutil
from os import system

ruta_recetas = Path.home()/ "Recetas"
#lee los archivos txt de las recetas. Los crea y escribe, y los elimina
def manipular_receta(categoria, receta, accion, cuerpo_receta=None):
    ruta = ruta_recetas / categoria / (receta + ".txt")
    if accion == "leer":
        archivo = open(ruta, "r")
        contenido = archivo.read()
        print(f"\n{contenido}\n")
        archivo.close()
    elif accion == "crear":
        archivo = open(ruta, "w")
        archivo.write(cuerpo_receta)
        print("\nReceta registrada\n")
        archivo.close()
    elif accion == "eliminar":
        ruta.unlink()
        print("\nReceta eliminada exitosamente\n")
    
    
#muestra los nombres de los archivos .txt correspondiente a las recetas dentro de una categoría específica
def mostrar_recetas(categoria):
    ruta = ruta_recetas / categoria
    
    for archivo in ruta.glob("*.txt"):
        print(archivo.stem)


def mostrar_categorías():
    print("Categorías:")
    for carpeta in ruta_recetas .iterdir():
        if carpeta.is_dir():
            print(carpeta.name)

def crear_categoria(nombre):
    ruta = ruta_recetas / nombre
    ruta.mkdir()
    print("\nCategoría creada\n")

def eliminar_categoria(nombre):
    ruta = ruta_recetas / nombre
    shutil.rmtree(ruta)
    print("\nCategoría eliminada\n")

def contar_recetas():
    return len(list(ruta_recetas.glob("**/*.txt")))

def mostrar_menu():
 
 opcion = input("""Elija una opción
 1- Ver receta
 2- Crear nueva receta
 3- Crear nueva categoría
 4- Eliminar receta
 5- Eliminar categoría
 6- Salir               
 """)
 return opcion

def bienvenida():
 print(f"""Bienvenido!
 La carpeta recetas se encuentra en {ruta_recetas}.
 Hay en total {contar_recetas()} recetas""")

bienvenida()    
opcion = mostrar_menu()

while opcion != "6":

    if opcion == "1":
        print("Ingrese el nombre correspondiente a la categoría de su receta\n")
        mostrar_categorías()
        categoria = input()
        print("\nIngrese el nombre de la receta que quiere mostrar\n")
        mostrar_recetas(categoria)
        receta = input()
        manipular_receta(categoria,receta,"leer")
    elif opcion == "2":
        print("\nIngrese el nombre correspondiente a la categoría de su receta\n")
        mostrar_categorías()
        categoria = input()
        nombre_nueva_receta = input("\nIngrese el nombre de la nueva receta\n")
        cuerpo_receta = input("\nIngrese el texto de la nueva receta\n")
        manipular_receta(categoria, nombre_nueva_receta, "crear", cuerpo_receta)
    elif opcion == "3":
        nombre_categoria = input("\nIngrese el nombre de la categoría que quiere crear\n")
        crear_categoria(nombre_categoria)
    elif opcion == "4":
        print("\nIngrese el nombre correspondiente a la categoría de su receta\n")
        mostrar_categorías()
        categoria = input()
        print("\n")
        mostrar_recetas(categoria)
        receta = input("\nIngrese el nombre de la receta que quiere eliminar\n")
        manipular_receta(categoria, receta, "eliminar")
    elif opcion == "5":
        mostrar_categorías()
        categoria = input("\nIngrese el nombre de la categoría que quiere eliminar\n")
        eliminar_categoria(categoria)
    
    
    input("\nPresione Enter para regresar al menú...")
    system("cls")
    opcion = mostrar_menu()
else:
    print("Programa finalizado")



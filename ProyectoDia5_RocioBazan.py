
lista_palabras = ["pizza","cerdo", "flores", "administracion", "mate", "rosa", "dorado", "chocolate", "oso"]

from random import choice

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    return palabra_elegida

def pedir_letra():
    while  True:
        letra = input("Elegí una letra ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("Ingrese sólo una letra válida")

def estado_palabra(palabra, letras_acertadas):
    
    for letra in palabra:
        return " ".join(letra if letra in letras_acertadas else "_" for letra in palabra)

def verificar_letra(letra, palabra, letras_acertadas):
    if letra in palabra:
        letras_acertadas.add(letra)
        return True
    else:
        return False

def detectar_ganador(palabra, letras_acertadas):
    if set(palabra) == letras_acertadas:
        return True
    return False

palabra = elegir_palabra(lista_palabras)
letras_acertadas = set()
vidas = 6
print("""Hola! Jugaremos al ahorcado.
Tienes que intentar adivinar la palabra secreta, letra por letra.
Tienes 6 intentos... comencemos!""")

while vidas > 0:
    print(f"Palabra: {estado_palabra(palabra,letras_acertadas)}")
    print(f"Tienes {vidas} vidas")

    letra = pedir_letra()

    if verificar_letra(letra, palabra, letras_acertadas):
        print(f"Correcto! la letra {letra} está en la palabra")
    else:
        print(f"La letra {letra} no está en la palabra :/ Pierdes una vida")
        vidas = vidas - 1

    if detectar_ganador(palabra, letras_acertadas):
        print(f"Ganaste! la palabra secreta es {palabra}")
        break
else:
    print("Lo siento! Agotaste todos los intentos")
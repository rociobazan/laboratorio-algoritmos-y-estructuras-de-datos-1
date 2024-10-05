nombre = input("¡Bienvenido!, ¿Cómo te llamas?")
print(f"Bueno, {nombre}. Pensé en un número del 1 al 100 y tienes sólo ocho intentos para adivinarlo...")
from random import randint
numero_pensado = randint(1,100)
cantidad_intentos = 1

while cantidad_intentos <= 8:
    numero_ingresado = int(input("¿Cuál crees que es el número? "))
    if numero_pensado == numero_ingresado:
        print(r'''
        |￣￣￣￣￣￣￣￣￣￣￣|
            ¡GANASTE!
        |＿＿＿＿＿＿＿＿＿＿＿| 
            (\__/)  ||
            (•ㅅ•)  ||
            / 　 づ
        ''')
        print(f"Ganaste! el número que pensé es {numero_pensado}. Lo adivinaste en el intento {cantidad_intentos}")
        break
    elif numero_ingresado < 1 or numero_ingresado > 100:
        print(r'''
        |￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
           ¡Número fuera de rango!
        |＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
            (\__/)  ||
            (•ㅅ•)  ||
            / 　 づ
        ''')
        print("El número que ingresaste está fuera de rango. Tiene que estar entre 0 y 100.")
    elif numero_ingresado > numero_pensado:
        print(r'''
        |￣￣￣￣￣￣￣￣￣￣￣|
         ¡Un poco más chico!
        |＿＿＿＿＿＿＿＿＿＿＿| 
            (\__/)  ||
            (•ㅅ•)  ||
            / 　 づ
        ''')
        print("Tu respuesta es incorrecta. El número que ingresaste es mayor al que pensé")
    else:
        print(r'''
        |￣￣￣￣￣￣￣￣￣￣￣|
          ¡Un poco más alto!
        |＿＿＿＿＿＿＿＿＿＿＿| 
            (\__/)  ||
            (•ㅅ•)  ||
            / 　 づ
        ''')
        print("Tu respuesta es incorrecta. El número que ingresaste es menor al que yo pensé")
    
    cantidad_intentos = cantidad_intentos + 1
else:
    print(r'''
    |￣￣￣￣￣￣￣￣￣￣￣￣|
       ¡Juego terminado!
    |＿＿＿＿＿＿＿＿＿＿＿＿|
        (\__/)  ||
        (•ㅅ•)  ||
        / 　 づ
    ''')
    print("El juego ha finalizado, agotaste los intentos.")

#---
print("Código de Rocío Bazán")
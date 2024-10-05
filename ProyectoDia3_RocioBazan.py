#1
texto = input("Ingrese un texto por favor").lower()
letras = input("Ingrese tres letras a elección separadas por espacios").lower()
lista_letras = letras.split()

contar_a = texto.count(lista_letras[0]) 
contar_b = texto.count(lista_letras[1])
contar_c = texto.count(lista_letras[2])

print(f"""La letra \"{lista_letras[0]}\" aparece {contar_a} veces.
La letra \"{lista_letras[1]}\" aparece {contar_b} veces.
La letra \"{lista_letras[2]}\" aparece {contar_c} veces """)

#2
lista_texto = texto.split()
cantidad_palabras = len(lista_texto)
print(f"El texto que ingresaste tiene {cantidad_palabras} palabras")

#3
primer_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es la \"{primer_letra}\"  y la última letra es la \"{ultima_letra}\"")

#4
lista_texto.reverse()
texto_reves = " ".join(lista_texto)
print(f"Si invertimos el orden de las palabras de tu texto, el resultado es: \"{texto_reves}\"")

#5
palabra = "Python"
encontrado = palabra.lower() in texto

resultado = {
    True: "La palabra \"python\" si forma parte de tu texto",
    False: "La palabra \"python\" no forma parte de tu texto"
}

print(resultado[encontrado])

#-----
print("Código de Rocío Bazan")
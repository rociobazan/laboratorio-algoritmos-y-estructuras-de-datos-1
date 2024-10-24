#ejercicio1

def devolver_distintos(a,b,c):
    if sum(a,b,c) > 15:
        return max(a,b,c)
    elif sum(a,b,c) < 10:
        return min(a,b,c)
    else:
        return sorted(1)
    
#ejercicio2

def letras_unicas(palabra):
    letras_unicas = sorted(set(palabra))
    return letras_unicas

#ejercicio3

def contar_ceros(*args):
    for num1, num2 in zip(args, args[1:]):
        if num1 == 0 and num2 == 0:
            return True
    return False

resultado = contar_ceros(1,0,0)
print(resultado)

#ejercicio 4

# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.

# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.

# Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(num):
    lista_numeros = list(range(num + 1))
    lista_numeros_primos = []
    contador_primos = 0

    for n in lista_numeros:
        if n < 2:
            continue
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
            
        if es_primo:
            lista_numeros_primos.append(n)
            contador_primos += 1

    print(f"Hay {contador_primos} números primos.Ellos son {lista_numeros_primos}")
    
    return contador_primos

contar_primos(20)
                
                
                

                



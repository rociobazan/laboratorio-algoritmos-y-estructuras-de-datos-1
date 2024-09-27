nombre = input("¡Bienvenido!, ¿Cuál es tu nombre?")
ventas = round(float(input(f"{nombre}, ingresa el monto correspondiente a tus ventas del período por favor.")),2)
comision = round(ventas * 0.13, 2)
print(f"""{nombre}, el monto de tu comisión es de ${comision}.
Tus ventas fueron de ${ventas} 
El monto total a cobrar es de ${ventas+comision}""")
#-----
print("Código de Rocío Bazan")


class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0.0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        

    def __str__(self):
        return f"""Cliente: {self.nombre} {self.apellido}
        Número de cuenta: {self.numero_cuenta}
        Balance: ${self.balance}\n"""

    def depositar(self, monto):
        self.balance += monto
        print(f"Su dinero se depositó correctamente. El saldo acutal es de ${self.balance} \n")

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            print(f"Retiro exitoso. El saldo actual es de {self.balance} \n")
        else:
            print("No posee saldo suficiente\n")


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    return Cliente(nombre, apellido, numero_cuenta)

def inicio():
    cliente = crear_cliente()
    print(f"Bienvenido {cliente.nombre} {cliente.apellido}")

    while True:
        print(cliente)
        print("Ingrese qué operación desea realizar")
        print("1- Depósito")
        print("2- Extracción")
        print("3-Salir")
        opcion = input()

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar \n"))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar \n"))
            cliente.retirar(monto)
        elif opcion == "3":
            print("Sesión finalizada")
        else:
            print("Ingrese una opción válida")


inicio()
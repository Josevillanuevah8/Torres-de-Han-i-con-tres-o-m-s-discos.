# Programa 2: Torres de Hanoi utilizando pilas

class Pila:
    def __init__(self, nombre):
        self.nombre = nombre
        self.discos = []

    def apilar(self, disco):
        if not self.esta_vacia() and self.discos[-1] < disco:
            raise ValueError("No puedes poner un disco grande sobre uno pequeno")

        self.discos.append(disco)

    def desapilar(self):
        if self.esta_vacia():
            raise ValueError("La torre esta vacia")

        return self.discos.pop()

    def esta_vacia(self):
        return len(self.discos) == 0


def mover_discos(n, origen, auxiliar, destino):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)

        print("Mover disco", disco, "de", origen.nombre,
              "a", destino.nombre)
    else:
        mover_discos(n - 1, origen, destino, auxiliar)

        mover_discos(1, origen, auxiliar, destino)

        mover_discos(n - 1, auxiliar, origen, destino)


print("JUEGO DE LAS TORRES DE HANOI")

try:
    cantidad = int(input("Ingresa la cantidad de discos (3 o mas): "))

    if cantidad < 3:
        print("Debes ingresar al menos 3 discos")
    else:
        torre_a = Pila("A")
        torre_b = Pila("B")
        torre_c = Pila("C")

        # Colocar todos los discos en la torre A
        for disco in range(cantidad, 0, -1):
            torre_a.apilar(disco)

        print("\nMovimientos para resolver el juego:")

        mover_discos(cantidad, torre_a, torre_b, torre_c)

        print("\nJuego terminado")
        print("Discos en la torre final:", torre_c.discos)
        print("Cantidad de movimientos:",
              2 ** cantidad - 1)

except ValueError as error:
    print("Error:", error)
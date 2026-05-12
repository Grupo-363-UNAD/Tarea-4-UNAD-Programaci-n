#Sistema gestor 

class SistemaGestion:

    # Esta clase no estaba en el código original

    # ✔ Sirve como "controlador central"
    # ✔ Organiza clientes, servicios y reservas
    # ✔ Evita código desordenado en el main

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        # Centraliza la gestión de clientes
        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        # Centraliza servicios disponibles
        self.servicios.append(servicio)

    def crear_reserva(self, reserva):
        # Centraliza reservas
        self.reservas.append(reserva)
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

# ==========================================================
# SERVICIOS DISPONIBLES (POLIMORFISMO)
# ==========================================================

servicios = [
    ReservaSala("Sala A", 50000),
    AlquilerEquipos("Computadores", 30000),
    Asesoria("Consultoría TI", 80000)
]

print("\n========== SERVICIOS DISPONIBLES ==========\n")

# Cada servicio implementa su propia versión de descripcion()
# Esto permite extender el sistema sin modificar este bloque
for s in servicios:
    print(s.descripcion())


# ==========================================================
# SISTEMA
# ==========================================================

#creación de un objeto controlador del sistema
# Antes el flujo era lineal sin organización
# Ahora el sistema centraliza clientes, servicios y reservas
sistema = SistemaGestion()
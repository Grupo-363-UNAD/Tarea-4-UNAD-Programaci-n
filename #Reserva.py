# ==========================================================
# CLASE RESERVA
# ==========================================================

class Reserva:

    def __init__(self, cliente, servicio, horas):

        try:
             # Validación estricta antes de asignar atributos
            if horas <= 0:
                raise ReservaError("Horas inválidas")

            if horas > 24:
                raise ReservaError("Máximo 24 horas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

            registrar_log("Reserva creada correctamente")

        except ReservaError as e:
            # Antes el error solo se imprimía
            # Ahora se registra y se detiene correctamente la creación
            registrar_log(str(e))
            raise

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def calcular_total(self):
        return self.servicio.calcular_coste(self.horas)

    def mostrar(self):
        print("\n--- RESERVA ---")
        print("Cliente:", self.cliente.get_nombre())
        print("Servicio:", self.servicio.nombre)
        print("Horas:", self.horas)
        print("Estado:", self.estado)
        print("Total:", self.calcular_total())
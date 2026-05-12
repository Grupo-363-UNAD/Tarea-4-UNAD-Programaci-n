#Reserva 

class Reserva:

    def __init__(self, cliente, servicio, horas):

        try:
            # Validación estricta antes de asignar atributos

            if horas <= 0:
                raise ReservaError("Horas inválidas")

            if horas > 24:
                raise ReservaError("Máximo 24 horas permitidas")

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

    def calcular_total(self, impuesto=0, descuento=0):

        # Ahora la reserva soporta lógica extendida
        # (impuestos y descuentos desde el servicio)
        return self.servicio.calcular_coste(self.horas, impuesto, descuento)
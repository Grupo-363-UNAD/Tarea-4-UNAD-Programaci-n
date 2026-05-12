# ==========================================================
# CLASE SERVICIO (ABSTRACTO)
# ==========================================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        # Validación estricta en el constructor
        # antes: el sistema podía crear objetos inválidos parcialmente
        if tarifa <= 0:
            raise ServicioError("Tarifa inválida")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def descripcion(self):
        pass

    def calcular_coste(self, horas, impuesto=0, descuento=0):

        total = horas * self.tarifa
        total += total * impuesto
        total -= total * descuento
        return total


# ==========================================================
# SERVICIOS CONCRETOS (POLIMORFISMO)
# ==========================================================

class ReservaSala(Servicio):
    def descripcion(self):
        return f"Sala de reuniones - {self.nombre} - ${self.tarifa}"


class AlquilerEquipos(Servicio):
    def descripcion(self):
        return f"Equipos - {self.nombre} - ${self.tarifa}"


class Asesoria(Servicio):
    def descripcion(self):
        return f"Asesoría - {self.nombre} - ${self.tarifa}"
    





        # Este método simula sobrecarga
        # Python no soporta sobrecarga real, por eso usamos parámetros opcionales

        base = horas * self.tarifa

        # Cálculo flexible con impuestos
        base += base * impuesto

        # Aplicación de descuentos opcionales
        base -= base * descuento

        return base
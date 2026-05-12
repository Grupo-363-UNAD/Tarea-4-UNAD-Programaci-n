#Servicio 

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        # Validación estricta en el constructor
        # antes: el sistema podía crear objetos inválidos parcialmente
        if tarifa <= 0:
            raise ServicioError("Tarifa inválida")

        self.nombre = nombre
        self.tarifa = tarifa

    def calcular_coste(self, horas, impuesto=0, descuento=0):

        # Este método simula sobrecarga
        # Python no soporta sobrecarga real, por eso usamos parámetros opcionales

        base = horas * self.tarifa

        # 🔥 NUEVO: cálculo flexible con impuestos
        base += base * impuesto

        # 🔥 NUEVO: aplicación de descuentos opcionales
        base -= base * descuento

        return base
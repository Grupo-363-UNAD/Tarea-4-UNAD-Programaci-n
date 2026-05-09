#Importar las librerias

from abc import ABC, abstractmethod
from datetime import datetime


# Función para registrar eventos en un archivo de logs

def registrar_log(mensaje):

    # Crear o abrir el archivo de logs en modo append
    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(
            f"{datetime.now()} -> {mensaje}\n"
        )


# =====================================================
# Excepciones Personalizadas
# =====================================================

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


# =====================================================
# Clase abstracta Persona
# =====================================================

class Persona(ABC):

    @abstractmethod
    def mostrar_datos(self):
        pass



# Clase cliente 

class Cliente(Persona):

    def __init__(self, nombre, correo):

        try:

            # Validar que el nombre no esté vacío
            if not nombre.strip():

                raise ClienteError(
                    "El nombre no puede estar vacío"
                )

            # Validar correo electrónico básico
            if "@" not in correo:

                raise ClienteError(
                    "Correo inválido"
                )

            # Atributos privados del cliente
            self.__nombre = nombre
            self.__correo = correo

        except Exception as e:

            registrar_log(
                f"Error Cliente: {e}"
            )

            raise

    # Mostrar datos del cliente
    def mostrar_datos(self):

        return (
            f"Cliente: "
            f"{self.__nombre} - {self.__correo}"
        )

    # Obtener nombre del cliente
    def get_nombre(self):

        return self.__nombre


# =====================================================
# Clase abstracta Servicio
# =====================================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass



# Reserva de las salas


class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        return self.tarifa * horas

    def descripcion(self):

        return (
            f"Servicio de reserva de salas "
            f"- Tarifa: {self.tarifa}"
        )



# Alquiler de los equipos


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        return self.tarifa * horas

    def descripcion(self):

        return (
            f"Servicio de alquiler de equipos "
            f"- Tarifa: {self.tarifa}"
        )



# Asesoría especializada para los clientes


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        return self.tarifa * horas

    def descripcion(self):

        return (
            f"Asesoría especializada "
            f"- Tarifa: {self.tarifa}"
        )



# Clase reserva que relaciona cliente, servicio y horas


class Reserva:

    def __init__(self, cliente, servicio, horas):

        try:

            # VALIDAR HORAS
            if horas <= 0:

                raise ReservaError(
                    "Las horas deben ser mayores "
                    "a cero"
                )

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except Exception as e:

            registrar_log(
                f"Error Reserva: {e}"
            )

            raise

    # Confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"

        registrar_log(
            "Reserva confirmada"
        )

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            "Reserva cancelada"
        )

    # Procesasr reserva y mostrar resultados
    def procesar_reserva(self):

        try:

            # Calcular costo del servicio
            costo = self.servicio.calcular_costo(
                self.horas
            )

            # Muestra resultados de la reserva
            print("\n===== RESERVA =====")

            print(
                "Cliente:",
                self.cliente.get_nombre()
            )

            print(
                "Servicio:",
                self.servicio.descripcion()
            )

            print("Costo:", costo)

            print("Estado:", self.estado)

            # Regitrar evento de reserva procesada
            registrar_log(
                f"Reserva procesada para "
                f"{self.cliente.get_nombre()}"
            )

        except Exception as e:

            registrar_log(
                f"Error Procesando Reserva: {e}"
            )

            print("Error:", e)



# Listar del sistema para clientes, servicios y reservas


clientes = []
servicios = []
reservas = []



# Registrar cliente en el sistema


while True:

    try:

        print("\n===== REGISTRO CLIENTE =====")

        # solicitar nombre del cliente
        nombre = input(
            "Ingrese nombre del cliente: "
        )

        # solicitar correo del cliente
        correo = input(
            "Ingrese correo del cliente: "
        )

        # Crea el cliente con los datos ingresados
        cliente1 = Cliente(nombre, correo)

        # Guarda el cliente en la lista de clientes
        clientes.append(cliente1)

        # Registrar evento de cliente registrado
        registrar_log(
            f"Cliente registrado: {nombre}"
        )

        print(
            "Cliente registrado correctamente"
        )

        break

    except Exception as e:

        print("Error:", e)

        registrar_log(
            f"Error Registro Cliente: {e}"
        )

        print(
            "Ingrese nuevamente "
            "los datos.\n"
        )



# Creacion del servicio en el sistema


while True:

    try:

        print("\n===== CREACION SERVICIO =====")

        print("1. Reserva Sala")
        print("2. Alquiler Equipos")
        print("3. Asesoria Especializada")

        # Opcion del servicio a crear
        opcion = int(
            input("Seleccione servicio: ")
        )

        # Nombre del servicio
        nombre_servicio = input(
            "Ingrese nombre del servicio: "
        )

        # Tarifa por hora del servicio
        tarifa = float(
            input(
                "Ingrese tarifa por hora: "
            )
        )

        # Reserva de salas
        if opcion == 1:

            servicio1 = ReservaSala(
                nombre_servicio,
                tarifa
            )

        # Alquiler de equipos
        elif opcion == 2:

            servicio1 = AlquilerEquipo(
                nombre_servicio,
                tarifa
            )

        # Aswsoria especializada
        elif opcion == 3:

            servicio1 = (
                AsesoriaEspecializada(
                    nombre_servicio,
                    tarifa
                )
            )

        else:

            raise ServicioError(
                "Opción inválida"
            )

        # GUARDAR SERVICIO
        servicios.append(servicio1)

        # Registrar evento de servicio creado
        registrar_log(
            f"Servicio creado: "
            f"{nombre_servicio}"
        )

        print(
            "Servicio creado correctamente"
        )

        break

    except Exception as e:

        print("Error:", e)

        registrar_log(
            f"Error Servicio: {e}"
        )

        print(
            "Ingrese nuevamente "
            "los datos del servicio.\n"
        )



# Creacion de reserva en el sistema


while True:

    try:

        print("\n===== CREAR RESERVA =====")

        # Solicitar horas de reserva
        horas = int(
            input(
                "Ingrese cantidad de horas: "
            )
        )

        # Crea reserva con el cliente, servicio y horas ingresados
        reserva1 = Reserva(
            cliente1,
            servicio1,
            horas
        )

        # Guardar reserva en la lista de reservas
        reservas.append(reserva1)

        print("\n1. Confirmar")
        print("2. Cancelar")

        # Estado dereserva a confirmar o cancelar
        estado = int(
            input(
                "Seleccione estado reserva: "
            )
        )

        # Confirmar reserva
        if estado == 1:

            reserva1.confirmar()

        # Cancelar reserva
        elif estado == 2:

            reserva1.cancelar()

        else:

            print("Opción inválida")

        # Procesar reserva y mostrar resultados
        reserva1.procesar_reserva()

        break

    except Exception as e:

        print("Error:", e)

        registrar_log(
            f"Error Reserva: {e}"
        )

        print(
            "Ingrese nuevamente "
            "los datos de la reserva.\n"
        )



# Muestra clientes registrados en el sistema


print("\n===== CLIENTES REGISTRADOS =====")

for cliente in clientes:

    print(cliente.mostrar_datos())



# Finaliza el sistema y muestra mensaje de despedida

registrar_log(
    "Sistema finalizado correctamente"
)

print("\n===== SISTEMA FINALIZADO =====")
input("Presiona Enter para salir...")
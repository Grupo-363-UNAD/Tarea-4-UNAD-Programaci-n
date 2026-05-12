# ==========================================================
# Sistema Integral de Gestión de Clientes,
# Servicios y Reservas
#
# Programación Orientada a Objetos
# Manejo de Excepciones
#
# Grupo: 363
# ==========================================================

from abc import ABC, abstractmethod


# ==========================================================
# ARCHIVO DE LOGS
# ==========================================================

def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


# ==========================================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================================

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


# ==========================================================
# CLASE CLIENTE
# ==========================================================

class Cliente:

    def __init__(self, nombre, documento, correo):

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

        self.validar_datos()

    # ------------------------------------------------------

    def validar_datos(self):

        try:

            if self.__nombre.strip() == "":
                raise ClienteError(
                    "El nombre no puede estar vacío"
                )

            if not str(self.__documento).isdigit():
                raise ClienteError(
                    "El documento debe contener solo números"
                )

            if "@" not in self.__correo or "." not in self.__correo:
                raise ClienteError(
                    "Correo electrónico inválido"
                )

        except ClienteError as e:

            print("Error:", e)
            registrar_log(str(e))

        else:

            print("Cliente registrado exitosamente")

        finally:

            print("Validación de cliente finalizada\n")

    # ------------------------------------------------------
    # GETTERS
    # ------------------------------------------------------

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    # ------------------------------------------------------

    def mostrar_cliente(self):

        print("----- CLIENTE -----")
        print("Nombre:", self.__nombre)
        print("Documento:", self.__documento)
        print("Correo:", self.__correo)


# ==========================================================
# CLASE ABSTRACTA SERVICIO
# ==========================================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if tarifa <= 0:
            raise ServicioError(
                "La tarifa debe ser mayor a cero"
            )

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def descripcion(self):
        pass


# ==========================================================
# HERENCIA Y POLIMORFISMO
# ==========================================================

class ReservaSala(Servicio):

    def descripcion(self):
        return f"Reserva de Sala - Tarifa: ${self.tarifa}"


class AlquilerEquipos(Servicio):

    def descripcion(self):
        return f"Alquiler de Equipos - Tarifa: ${self.tarifa}"


class Asesoria(Servicio):

    def descripcion(self):
        return f"Asesoría Personalizada - Tarifa: ${self.tarifa}"


# ==========================================================
# CLASE RESERVA
# ==========================================================

class Reserva:

    def __init__(self, cliente, servicio, horas):

        try:

            if horas <= 0:
                raise ReservaError(
                    "Las horas deben ser mayores a cero"
                )

            if horas > 24:
                raise ReservaError(
                    "No se permiten reservas mayores a 24 horas"
                )

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except ReservaError as e:

            print("Error:", e)
            registrar_log(str(e))

        else:

            print("Reserva creada correctamente")

        finally:

            print("Proceso de reserva finalizado\n")

    # ------------------------------------------------------

    def confirmar(self):

        self.estado = "Confirmada"

        print(
            f"Reserva confirmada para "
            f"{self.cliente.get_nombre()}"
        )

    # ------------------------------------------------------

    def cancelar(self):

        self.estado = "Cancelada"

        print(
            f"Reserva cancelada para "
            f"{self.cliente.get_nombre()}"
        )

    # ------------------------------------------------------

    def calcular_total(self):

        return self.horas * self.servicio.tarifa

    # ------------------------------------------------------

    def mostrar_reserva(self):

        print("----- RESERVA -----")
        print("Cliente:", self.cliente.get_nombre())
        print("Servicio:", self.servicio.nombre)
        print("Horas:", self.horas)
        print("Estado:", self.estado)
        print("Costo Total:", self.calcular_total())


# ==========================================================
# LISTA DE SERVICIOS (POLIMORFISMO)
# ==========================================================

servicios = [

    ReservaSala("Sala de Juntas", 50000),
    AlquilerEquipos("Computadores", 30000),
    Asesoria("Asesoría Técnica", 80000)

]

print("\n========== SERVICIOS DISPONIBLES ==========\n")

for servicio in servicios:

    print(servicio.descripcion())


# ==========================================================
# PRUEBAS DEL SISTEMA
# ==========================================================

print("\n========== PRUEBAS CLIENTES ==========\n")

cliente1 = Cliente(
    "Santiago",
    "123456",
    "santiago@gmail.com"
)

cliente2 = Cliente(
    "",
    "654321",
    "correo@gmail.com"
)

cliente3 = Cliente(
    "Carlos",
    "ABC123",
    "carlos@gmail.com"
)

cliente4 = Cliente(
    "Laura",
    "987654",
    "lauragmail.com"
)


# ==========================================================
# PRUEBAS SERVICIOS
# ==========================================================

print("\n========== PRUEBAS SERVICIOS ==========\n")

try:

    servicio_error = ReservaSala(
        "Sala VIP",
        -5000
    )

except ServicioError as e:

    print("Error:", e)
    registrar_log(str(e))


# ==========================================================
# PRUEBAS RESERVAS
# ==========================================================

print("\n========== PRUEBAS RESERVAS ==========\n")

reserva1 = Reserva(
    cliente1,
    servicios[0],
    3
)

reserva1.confirmar()

reserva1.mostrar_reserva()

print()

reserva2 = Reserva(
    cliente1,
    servicios[1],
    30
)

print()

reserva3 = Reserva(
    cliente1,
    servicios[2],
    -2
)

print()

reserva1.cancelar()


# ==========================================================
# FIN DEL PROGRAMA
# ==========================================================

print("\nSistema finalizado correctamente")



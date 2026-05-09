# =====================================================
# IMPORTACION DE LIBRERIAS
# =====================================================

from abc import ABC, abstractmethod
from datetime import datetime


# =====================================================
# FUNCION PARA REGISTRAR LOGS
# =====================================================

def registrar_log(mensaje):

    # CREA Y GUARDA EVENTOS EN logs.txt
    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(
            f"{datetime.now()} -> {mensaje}\n"
        )


# =====================================================
# EXCEPCIONES PERSONALIZADAS
# =====================================================

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


# =====================================================
# CLASE ABSTRACTA PERSONA
# =====================================================

class Persona(ABC):

    @abstractmethod
    def mostrar_datos(self):
        pass


# =====================================================
# CLASE CLIENTE
# =====================================================

class Cliente(Persona):

    def __init__(self, nombre, correo):

        try:

            # VALIDAR NOMBRE
            if not nombre.strip():

                raise ClienteError(
                    "El nombre no puede estar vacío"
                )

            # VALIDAR CORREO
            if "@" not in correo:

                raise ClienteError(
                    "Correo inválido"
                )

            # ATRIBUTOS PRIVADOS
            self.__nombre = nombre
            self.__correo = correo

        except Exception as e:

            registrar_log(
                f"Error Cliente: {e}"
            )

            raise

    # MOSTRAR DATOS
    def mostrar_datos(self):

        return (
            f"Cliente: "
            f"{self.__nombre} - {self.__correo}"
        )

    # OBTENER NOMBRE
    def get_nombre(self):

        return self.__nombre


# =====================================================
# CLASE ABSTRACTA SERVICIO
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


# =====================================================
# RESERVA DE SALAS
# =====================================================

class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        return self.tarifa * horas

    def descripcion(self):

        return (
            f"Servicio de reserva de salas "
            f"- Tarifa: {self.tarifa}"
        )


# =====================================================
# ALQUILER DE EQUIPOS
# =====================================================

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        return self.tarifa * horas

    def descripcion(self):

        return (
            f"Servicio de alquiler de equipos "
            f"- Tarifa: {self.tarifa}"
        )


# =====================================================
# ASESORIA ESPECIALIZADA
# =====================================================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        return self.tarifa * horas

    def descripcion(self):

        return (
            f"Asesoría especializada "
            f"- Tarifa: {self.tarifa}"
        )


# =====================================================
# CLASE RESERVA
# =====================================================

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

    # CONFIRMAR RESERVA
    def confirmar(self):

        self.estado = "Confirmada"

        registrar_log(
            "Reserva confirmada"
        )

    # CANCELAR RESERVA
    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            "Reserva cancelada"
        )

    # PROCESAR RESERVA
    def procesar_reserva(self):

        try:

            # CALCULAR COSTO
            costo = self.servicio.calcular_costo(
                self.horas
            )

            # MOSTRAR RESULTADOS
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

            # REGISTRAR EVENTO
            registrar_log(
                f"Reserva procesada para "
                f"{self.cliente.get_nombre()}"
            )

        except Exception as e:

            registrar_log(
                f"Error Procesando Reserva: {e}"
            )

            print("Error:", e)


# =====================================================
# LISTAS DEL SISTEMA
# =====================================================

clientes = []
servicios = []
reservas = []


# =====================================================
# REGISTRO CLIENTE
# =====================================================

while True:

    try:

        print("\n===== REGISTRO CLIENTE =====")

        # SOLICITAR NOMBRE
        nombre = input(
            "Ingrese nombre del cliente: "
        )

        # SOLICITAR CORREO
        correo = input(
            "Ingrese correo del cliente: "
        )

        # CREAR CLIENTE
        cliente1 = Cliente(nombre, correo)

        # GUARDAR CLIENTE
        clientes.append(cliente1)

        # REGISTRAR EVENTO
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


# =====================================================
# CREACION SERVICIO
# =====================================================

while True:

    try:

        print("\n===== CREACION SERVICIO =====")

        print("1. Reserva Sala")
        print("2. Alquiler Equipos")
        print("3. Asesoria Especializada")

        # OPCION SERVICIO
        opcion = int(
            input("Seleccione servicio: ")
        )

        # NOMBRE SERVICIO
        nombre_servicio = input(
            "Ingrese nombre del servicio: "
        )

        # TARIFA SERVICIO
        tarifa = float(
            input(
                "Ingrese tarifa por hora: "
            )
        )

        # RESERVA SALA
        if opcion == 1:

            servicio1 = ReservaSala(
                nombre_servicio,
                tarifa
            )

        # ALQUILER EQUIPOS
        elif opcion == 2:

            servicio1 = AlquilerEquipo(
                nombre_servicio,
                tarifa
            )

        # ASESORIA
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

        # REGISTRAR EVENTO
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


# =====================================================
# CREAR RESERVA
# =====================================================

while True:

    try:

        print("\n===== CREAR RESERVA =====")

        # SOLICITAR HORAS
        horas = int(
            input(
                "Ingrese cantidad de horas: "
            )
        )

        # CREAR RESERVA
        reserva1 = Reserva(
            cliente1,
            servicio1,
            horas
        )

        # GUARDAR RESERVA
        reservas.append(reserva1)

        print("\n1. Confirmar")
        print("2. Cancelar")

        # ESTADO RESERVA
        estado = int(
            input(
                "Seleccione estado reserva: "
            )
        )

        # CONFIRMAR
        if estado == 1:

            reserva1.confirmar()

        # CANCELAR
        elif estado == 2:

            reserva1.cancelar()

        else:

            print("Opción inválida")

        # PROCESAR RESERVA
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


# =====================================================
# MOSTRAR CLIENTES
# =====================================================

print("\n===== CLIENTES REGISTRADOS =====")

for cliente in clientes:

    print(cliente.mostrar_datos())


# =====================================================
# FINALIZACION SISTEMA
# =====================================================

registrar_log(
    "Sistema finalizado correctamente"
)

print("\n===== SISTEMA FINALIZADO =====")
input("Presiona Enter para salir...")
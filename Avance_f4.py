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
# LOGGING (registro de eventos y errores)
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

class OperacionError(Exception):
    pass


# ==========================================================
# CLASE CLIENTE
# ==========================================================

class Cliente:

    def __init__(self, nombre, documento, correo):

        try:
            self.__nombre = nombre
            self.__documento = documento
            self.__correo = correo

            # 🔴 CAMBIO: ahora la validación está separada
            # 🟡 mejora: permite reutilización y control de errores
            self.validar_datos()

            # 🔴 CAMBIO: log de éxito agregado
            # 🟡 mejora: el sistema registra operaciones correctas (no solo errores)
            registrar_log(f"Cliente creado: {nombre}")

        except ClienteError as e:
            # 🔴 CAMBIO: se agrega logging + re-lanzamiento
            # 🟡 mejora: el sistema no oculta errores, los propaga correctamente
            registrar_log(f"ERROR Cliente: {e}")
            raise ClienteError(str(e)) from e

    def validar_datos(self):

        # 🔴 CAMBIO: validación estricta sin imprimir dentro del método
        # 🟡 mejora: separación de lógica y presentación (buen OOP)

        if not self.__nombre.strip():
            raise ClienteError("Nombre vacío")

        if not str(self.__documento).isdigit():
            raise ClienteError("Documento inválido")

        if "@" not in self.__correo or "." not in self.__correo:
            raise ClienteError("Correo inválido")

    # GETTERS (encapsulación)
    def get_nombre(self):
        return self.__nombre


# ==========================================================
# CLASE ABSTRACTA SERVICIO
# ==========================================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        # 🔴 CAMBIO: validación centralizada en constructor
        # 🟡 mejora: evita crear servicios inválidos desde el inicio

        if tarifa <= 0:
            raise ServicioError("Tarifa inválida")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def calcular_costo(self):
        pass


# ==========================================================
# HERENCIA + POLIMORFISMO (SERVICIOS)
# ==========================================================

class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa, horas=1):
        super().__init__(nombre, tarifa)
        self.horas = horas

    def descripcion(self):
        return f"Sala: {self.nombre}"

    # 🔴 CAMBIO: método con lógica específica por tipo de servicio
    # 🟡 mejora: POLIMORFISMO real (cada servicio calcula distinto)
    def calcular_costo(self, impuesto=0.19):
        return self.tarifa * self.horas * (1 + impuesto)


class AlquilerEquipos(Servicio):

    def __init__(self, nombre, tarifa, cantidad=1):
        super().__init__(nombre, tarifa)
        self.cantidad = cantidad

    def descripcion(self):
        return f"Equipos: {self.nombre}"

    def calcular_costo(self, descuento=0.1):
        return self.tarifa * self.cantidad * (1 - descuento)


class Asesoria(Servicio):

    def __init__(self, nombre, tarifa, horas=1):
        super().__init__(nombre, tarifa)
        self.horas = horas

    def descripcion(self):
        return f"Asesoría: {self.nombre}"

    def calcular_costo(self, impuesto=0.15, descuento=0):
        return self.tarifa * self.horas * (1 + impuesto - descuento)


# ==========================================================
# CLASE RESERVA
# ==========================================================

class Reserva:

    def __init__(self, cliente, servicio, horas):

        try:
            # 🔴 CAMBIO: validación estricta antes de asignar atributos
            # 🟡 mejora: evita estados inconsistentes del objeto

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
            # 🔴 CAMBIO: logging + rethrow
            # 🟡 mejora: trazabilidad del error sin perder control del sistema
            registrar_log(f"ERROR Reserva: {e}")
            raise ReservaError(str(e)) from e

    def confirmar(self):

        try:
            self.estado = "Confirmada"

            # 🔴 CAMBIO: uso de polimorfismo del servicio
            total = self.servicio.calcular_costo()

            registrar_log(f"Reserva confirmada: {total}")
            return total

        except Exception as e:
            # 🔴 CAMBIO: encapsulación del error genérico
            # 🟡 mejora: control de fallos inesperados
            registrar_log(f"ERROR confirmación: {e}")
            raise OperacionError("Error al confirmar") from e

    def cancelar(self):

        # 🔴 CAMBIO: validación de estado antes de cancelar
        # 🟡 mejora: evita operaciones inválidas
        if self.estado == "Cancelada":
            raise OperacionError("Ya cancelada")

        self.estado = "Cancelada"
        registrar_log("Reserva cancelada")

    def calcular_total(self):
        return self.servicio.calcular_costo()


# ==========================================================
# SISTEMA CENTRAL (GESTOR DEL PROYECTO)
# ==========================================================

class SistemaFJ:

    def __init__(self):
        self.clientes = []
        self.reservas = []

    def ejecutar(self):

        print("\n===== INICIO SIMULACIÓN =====\n")

        # 🔴 CAMBIO IMPORTANTE: todo el sistema ahora está centralizado
        # 🟡 mejora: cumple arquitectura modular del enunciado

        # 1 cliente válido
        c1 = Cliente("Kevin", "12345", "kevin@mail.com")
        self.clientes.append(c1)

        # 2 cliente inválido (controlado)
        try:
            Cliente("", "ABC", "correo")
        except:
            pass

        # 3 servicios
        s1 = ReservaSala("Sala A", 50000, 2)
        s2 = AlquilerEquipos("PCs", 30000, 3)
        s3 = Asesoria("Python", 80000, 2)

        # 4 reserva válida
        r1 = Reserva(c1, s1, 2)
        r1.confirmar()
        self.reservas.append(r1)

        # 5 reserva inválida
        try:
            Reserva(c1, s1, -1)
        except:
            pass

        # 6 reserva equipos
        r2 = Reserva(c1, s2, 1)
        r2.confirmar()

        # 7 asesoría
        r3 = Reserva(c1, s3, 2)
        r3.confirmar()

        # 8 cancelación válida
        r1.cancelar()

        # 9 error controlado
        try:
            r1.cancelar()
        except:
            pass

        # 10 evento final
        registrar_log("Simulación completa")


# ==========================================================
# EJECUCIÓN DEL SISTEMA
# ==========================================================

app = SistemaFJ()
app.ejecutar()

print("\nSistema finalizado correctamente")
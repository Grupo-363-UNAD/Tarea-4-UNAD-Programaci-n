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
# LOGS
# ==========================================================

def registrar_log(mensaje):

    try:
        # Ahora el log es más seguro
        # Antes podía fallar sin control

        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")

    except Exception as e:
        # Manejo de fallo crítico de logs
        print("Error crítico en logs:", e)


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
# CLASE BASE ABSTRACTA
# ==========================================================

class EntidadBase(ABC):

    @abstractmethod
    def mostrar(self):
        pass


# ==========================================================
# CLIENTE
# ==========================================================

class Cliente(EntidadBase):

    def __init__(self, nombre, documento, correo):

        #Cambie los atributos para que empiecen en None por que 
        # primero validamos antes de asignar valores reales 
        self.__nombre = None
        self.__documento = None
        self.__correo = None

        #Delege la validación a un método separado 
        self.set_datos(nombre, documento, correo)

    def set_datos(self, nombre, documento, correo):

        try:

            #Se mejoran las validaciones antes de crear el objeto 
            if not nombre or nombre.strip() == "":
                raise ClienteError("Nombre inválido")

            if not str(documento).isdigit():
                raise ClienteError("Documento inválido")

            if "@" not in correo or "." not in correo:
                raise ClienteError("Correo inválido")

            #Cambie a solo asignar si todo es válido
            self.__nombre = nombre
            self.__documento = documento
            self.__correo = correo

            registrar_log(f"Cliente creado: {nombre}")

        except ClienteError as e:
            #Cambie para que ahora el error se registre y se propague antes solo
            #se imprimia y el objeto seguia existiendo 
            registrar_log(str(e))
            raise

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    def mostrar(self):
        print("\n--- CLIENTE ---")
        print(self.__nombre, self.__documento, self.__correo)


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


# ==========================================================
# SISTEMA DE GESTIÓN
# ==========================================================

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
# SERVICIOS DISPONIBLES
# ==========================================================

servicios = [
    ReservaSala("Sala A", 50000),
    AlquilerEquipos("Computadores", 30000),
    Asesoria("Consultoría TI", 80000)
]

print("\n========== SERVICIOS DISPONIBLES ==========\n")

for s in servicios:
    print(s.descripcion())


# ==========================================================
# SISTEMA
# ==========================================================

sistema = SistemaGestion()


# ==========================================================
# PRUEBA CLIENTES
# ==========================================================

print("\n========== CLIENTES ==========\n")

try:
    # Validación dentro de la clase Cliente
    # Si el cliente es inválido, se lanza excepción automáticamente
    c1 = Cliente("Santiago", "123456", "santiago@gmail.com")
    sistema.agregar_cliente(c1)
    c1.mostrar()

except Exception as e:
    # El sistema no se detiene por errores de datos
    # Se permite continuar la ejecución (robustez del sistema)

    print(e)

try:
    # Prueba de entrada inválida
    # Permite demostrar manejo de excepciones
    c2 = Cliente("", "ABC", "correo")

except Exception as e:
     # Captura controlada del error sin afectar el flujo
    print(e)

try:
    c3 = Cliente("Laura", "987654", "laura@gmail.com")
    sistema.agregar_cliente(c3)
    c3.mostrar()
except Exception as e:
    print(e)


# ==========================================================
# RESERVAS
# ==========================================================

print("\n========== RESERVAS ==========\n")

# ---------------- RESERVA VÁLIDA ----------------
try:
    # Integración completa Cliente + Servicio + Reserva
    # Demuestra relación entre clases (POO real)
    r1 = Reserva(c1
    , servicios[0], 3)
    r1.confirmar()
    sistema.agregar_reserva(r1)

    print("\n--- RESERVA VÁLIDA ---")
    r1.mostrar()

except Exception as e:
    registrar_log(str(e))
    print(f"[ERROR CONTROLADO] {e}")


# Separador visual (MEJORA CLARA)
print("\n--- VALIDACIÓN DE RESERVAS INVÁLIDAS ---\n")


# ---------------- RESERVA INVÁLIDA 1 ----------------
try:
    #Validación de límite superior de negocio
    #(no más de 24 horas)
    r2 = Reserva(c1, servicios[1], 30)

except Exception as e:
    # Manejo de error sin interrumpir el sistema
    registrar_log(str(e))
    print(f"[ERROR CONTROLADO] {e}")


# ---------------- RESERVA INVÁLIDA 2 ----------------
try:
    # Validación de datos negativos
    r3 = Reserva(c1, servicios[2], -2)
except Exception as e:
    registrar_log(str(e))
    print(f"[ERROR CONTROLADO] {e}")


print("\nSistema finalizado correctamente")


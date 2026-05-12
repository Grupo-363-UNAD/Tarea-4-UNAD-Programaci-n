#Clase

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


# ==========================================================
# CLASE BASE ABSTRACTA
# ==========================================================

    class EntidadBase(ABC):

        @abstractmethod
        def mostrar(self):
            pass


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
            raise  # 🔥 importante: no ocultar error
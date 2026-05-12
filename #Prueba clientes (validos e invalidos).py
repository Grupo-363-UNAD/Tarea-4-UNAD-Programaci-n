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

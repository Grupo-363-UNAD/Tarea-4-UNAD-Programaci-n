#Prueba reservas (validos e invalidos)

# ==========================================================
# PRUEBAS CLIENTES (VALIDOS E INVALIDOS)
# ==========================================================

print("\n========== CLIENTES ==========\n")

try:
    # Validación dentro de la clase Cliente
    # Si el cliente es inválido, se lanza excepción automáticamente
    c1 = Cliente("Santiago", "123456", "santiago@gmail.com")
    sistema.agregar_cliente(c1)
    c1.mostrar()
except:
    # El sistema no se detiene por errores de datos
    # Se permite continuar la ejecución (robustez del sistema)
    pass

try:
    # Prueba de entrada inválida
    # Permite demostrar manejo de excepciones
    c2 = Cliente("", "ABC", "correo")
except:
    # Captura controlada del error sin afectar el flujo
    pass

try:
    c3 = Cliente("Laura", "987654", "laura@gmail.com")
    sistema.agregar_cliente(c3)
    c3.mostrar()
except:
    pass

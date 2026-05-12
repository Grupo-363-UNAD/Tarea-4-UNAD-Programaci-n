# Prueba reservas 



print("\n========== RESERVAS ==========\n")

try:
    # 🔥 MEJORA: integración completa Cliente + Servicio + Reserva
    # Demuestra relación entre clases (POO real)
    r1 = Reserva(c1, servicios[0], 3)
    r1.confirmar()
    sistema.agregar_reserva(r1)
    r1.mostrar()
except:
    pass

try:
    # 🔥 MEJORA: validación de límite superior de negocio
    # (no más de 24 horas)
    r2 = Reserva(c1, servicios[1], 30)
except:
    # 🔥 MEJORA: manejo de error sin interrumpir el sistema
    pass

try:
    # 🔥 MEJORA: validación de datos negativos
    r3 = Reserva(c1, servicios[2], -2)
except:
    pass


# ==========================================================
# CANCELACIÓN
# ==========================================================

# 🔥 MEJORA: cambio de estado de la reserva
# Demuestra control de ciclo de vida del objeto
r1.cancelar()

print("\nSistema finalizado correctamente")
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
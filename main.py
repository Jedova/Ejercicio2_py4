from membresia import Membresia
from membresia import Gratis, Basico, Familiar, SinConexion, Pro

def crear_membresia(correo, tarjeta, tipo):
    if tipo == 0:
        return Gratis(correo, tarjeta)
    elif tipo == 1:
        return Basico(correo, tarjeta)
    elif tipo == 2:
        return Familiar(correo, tarjeta)
    elif tipo == 3:
        return SinConexion(correo, tarjeta)
    elif tipo == 4:
        return Pro(correo, tarjeta)
    else:
        print("Opción inválida. Se asigna membresía Gratis por defecto.")
        return Gratis(correo, tarjeta)

# Se requiere
correo = input("Indica tu correo: ")
tarjeta = input("Indica el número de tarjeta: ")
tipo = int(input("Elige tipo de membresía (0-4): "))

compra = crear_membresia(correo, tarjeta, tipo)

print(f"\nCorreo: {compra.correo}")
print(f"Tarjeta: {compra.tarjeta}")
print(f"Tipo de membresía: {compra.__class__.__name__}")





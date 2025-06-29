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

##Ahora si buscamos ajustar membresía##

cambio = input(f"¿deseas cambiar de tu membresía {compra.__class__.__name__}? SI/NO: ").strip().upper()

if cambio == "SI":
    try:
        
        tipo2 = int(input("Elige tipo de membresía, la cual debe ser distinta a la actual (0: Gratis; 1: Básico; 2:Familiar; 3: Sin Conexión; 4: Pro): "))
        
        ##Validar el tipo
        if tipo2 not in [0,1,2,3,4]:
            print("Tipo de membresía no válido. No se realiza el cambio.")
        elif tipo2 == tipo:
            print (f"No puedes cambiar a la misma membresía. Se mantiene:  {compra.__class__.__name__} ")
        else:
            compra = crear_membresia(compra.correo, compra.tarjeta, tipo2)
            print(f"Tu nueva membresía es: {compra.__class__.__name__}")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entre 0 y 4.")
else:
    print(f"Tu membresía sigue siendo: {compra.__class__.__name__}")




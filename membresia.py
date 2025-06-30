##Membresias##
##Gratis, Básica, Familiar, Sin Conexión y Pro.
##Todos permiten el cambio de suscripción
##todos piden correo y n° de tarjeta

from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo, tarjeta):
        self.__correo = correo
        self.__tarjeta = tarjeta

    @property
    def correo(self):
        return self.__correo

    @property
    def tarjeta(self):
        return self.__tarjeta

####CLASES HIJAS###

class Gratis(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self._costo = 0
        self._dispositivos = 1

    def cambiar_suscripcion(self, tipo):
        if tipo in [1, 2, 3, 4]:  # tipos permitidos para Gratis, considerando que Gratis es 0
            return crear_membresia(self.correo, self.tarjeta, tipo)
        return self
    
    def ver_info(self):
        print(f"\n  Información de membresía: {self.__class__.__name__}")
        print(f"Correo: {self.correo}")
        print(f"Tarjeta: {self.tarjeta}")
        print(f"Costo mensual: $ {self._costo}")
        print(f"Dispositivos permitidos: {self._dispositivos}")


class Basico(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self._costo = 3000
        self._dispositivos = 2
    
    def cambiar_suscripcion(self, tipo):
        if tipo in [0, 2, 3, 4]:  # tipos permitidos para Básico, considerando que Básico es 1
            return crear_membresia(self.correo, self.tarjeta, tipo)
        return self
    
    def ver_info(self):
        print(f"\n  Información de membresía: {self.__class__.__name__}")
        print(f"Correo: {self.correo}")
        print(f"Tarjeta: {self.tarjeta}")
        print(f"Costo mensual: $ {self._costo}")
        print(f"Dispositivos permitidos: {self._dispositivos}")


class Familiar(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self._costo = 5000
        self._dispositivos = 5
        self.dias_regalo= 7

    def cambiar_suscripcion(self, tipo):
        if tipo in [0, 1, 3, 4]:  # tipos permitidos para Familiar, considerando que Familiar es 2
            return crear_membresia(self.correo, self.tarjeta, tipo)
        return self
    
    def control_parental(self):
        pass

    def ver_info(self):
        print(f"\n  Información de membresía: {self.__class__.__name__}")
        print(f"Correo: {self.correo}")
        print(f"Tarjeta: {self.tarjeta}")
        print(f"Costo mensual: $ {self._costo}")
        print(f"Dispositivos permitidos: {self._dispositivos}")
        print(f"Días de regalo: {self.dias_regalo}")

class SinConexion(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self._costo = 3500
        self._dispositivos = 2
        self.dias_regalo= 7
    
    def cambiar_suscripcion(self, tipo):
        if tipo in [0, 1, 2, 4]:  # tipos permitidos para SinConexión, considerando que SinConexión es 3
            return crear_membresia(self.correo, self.tarjeta, tipo)
        return self
    
    def contenido_offline(self):
        pass

    def ver_info(self):
        print(f"\n  Información de membresía: {self.__class__.__name__}")
        print(f"Correo: {self.correo}")
        print(f"Tarjeta: {self.tarjeta}")
        print(f"Costo mensual: $ {self._costo}")
        print(f"Dispositivos permitidos: {self._dispositivos}")
        print(f"Días de regalo: {self.dias_regalo}")

class Pro(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self._costo = 7000
        self._dispositivos = 6
        self.dias_regalo= 15
    
    def cambiar_suscripcion(self, tipo):
        if tipo in [0, 1, 2, 3]:  # tipos permitidos para Pro, considerando que Pro es 4
            return crear_membresia(self.correo, self.tarjeta, tipo)
        return self
    
    def control_parental(self):
        pass

    def contenido_offline(self):
        pass

    def ver_info(self):
        print(f"\n  Información de membresía: {self.__class__.__name__}")
        print(f"Correo: {self.correo}")
        print(f"Tarjeta: {self.tarjeta}")
        print(f"Costo mensual: $ {self._costo}")
        print(f"Dispositivos permitidos: {self._dispositivos}")
        print(f"Días de regalo: {self.dias_regalo}")

##Nuevas membresías##
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


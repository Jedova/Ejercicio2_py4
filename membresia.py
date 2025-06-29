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

   
class Gratis(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self._costo = 0
        self._dispositivos = 1


class Basico(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self.costo = 3000
        self.dispositivos = 2

class Familiar(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self.costo = 5000
        self.dispositivos = 7

class SinConexion(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self.costo = 3500
        self.dispositivos = 2

class Pro(Membresia):
    def __init__(self, correo, tarjeta):
        super().__init__(correo, tarjeta)
        self.costo = 7000
        self.dispositivos = 6


from logger_base import log
class Persona:
    def __init__(self, idPersona=None, nombre=None, apellido=None, email=None):
        self._idPersona = idPersona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def idPersona(self):
        return self._idPersona

    @idPersona.setter
    def idPersona(self, value):
        self._idPersona = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def __str__(self):
        return f'''
            Id Persona: {self._idPersona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}
        '''

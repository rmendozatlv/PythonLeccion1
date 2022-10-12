from Cursor import CursorDelPool
from Persona import Persona
from logger_base import log


class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (CREATE-READ-UPDATE-DELETE)
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY idpersona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s , apellido = %s , email = %s WHERE idpersona = %s'
    _ELIMINAR = 'DELETE FROM persona WHERE idpersona = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertarPersona(cls, persona):
        with CursorDelPool() as cursor:
            values = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, values)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizarPersona(cls, persona):
        with CursorDelPool() as cursor:
            values = (persona.nombre, persona.apellido, persona.email, persona.idPersona)
            cursor.execute(cls._ACTUALIZAR, values)
            log.debug(f'Persona Actualizada Correctamente : {persona}')
            return cursor.rowcount

    @classmethod
    def eliminarPersona(cls, persona):
        with CursorDelPool() as cursor:
            values = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR, values)
            log.debug(f'Persona Eliminada Correctamente : {persona}')
            return cursor.rowcount


if __name__ == '__main__':
    # persona = Persona(6, "Jaimito", "Rodriguez", "jrodriguez@email.com")
    # log.debug(f"Registros Eliminados : {PersonaDAO.eliminarPersona(persona)}")

    for persona in PersonaDAO.seleccionar():
        log.debug(persona)

    persona1 = Persona(nombre='Diana', apellido='Mendez', email='dmendez@email.com')
    rows = PersonaDAO.insertarPersona(persona1)
    log.debug(f'Registros insertados : {rows}')


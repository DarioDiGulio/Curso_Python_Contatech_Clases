from abc import ABC, abstractmethod
from OOP_II.CustomErrors import InvalidAgeError, InvalidNameError


class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self) -> str:
        return self._nombre

    def es_mayor_edad(self):
        if self._edad < 0 or self._edad > 150:
            raise InvalidAgeError
        return self._edad >= 18


class Usuarios(ABC):

    @abstractmethod
    def guardar(self, usuario: Persona) -> None:
        pass

    @abstractmethod
    def obtener(self, nombre: str) -> Persona:
        pass


class UsuariosSQL(Usuarios):
    def obtener(self, nombre: str) -> Persona:
        pass

    def guardar(self, usuario: Persona) -> None:
        print(f'Guardando el usuario {usuario.get_nombre()}')
        print('Guardado.')


class UsuariosMongo(Usuarios):
    def obtener(self, nombre: str) -> Persona:
        pass

    def guardar(self, usuario: Persona) -> None:
        print(f'Archivando el usuario {usuario.get_nombre()}')
        print('Archivado.')


class Signup:
    def __init__(self, usuarios: Usuarios) -> None:
        self._usuarios = usuarios

    def guardar_usuario(self, usuario: Persona) -> bool:
        if usuario.es_mayor_edad():
            self._usuarios.guardar(usuario)
            return True
        else:
            return False


if __name__ == '__main__':
    usuario1 = Persona("Juan", 25)
    usuario2 = Persona("Maria", 25)
    usuario3 = Persona("José", -2)
    tabla_usuarios = UsuariosMongo()
    signup = Signup(tabla_usuarios)
    try:
        signup.guardar_usuario(usuario1)
        signup.guardar_usuario(usuario2)
        signup.guardar_usuario(usuario3)
    except InvalidAgeError:
        print(InvalidAgeError.message)

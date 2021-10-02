class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self) -> str:
        return self._nombre


class Auto:
    def __init__(self, marca: str, modelo: str, duenio: Persona) -> None:
        self._marca = marca
        self._modelo = modelo
        self._duenio = duenio

    def mostrar_duenio(self):
        print(f'El nombre de mi dueño es: {self._duenio.get_nombre()}')


if __name__ == '__main__':
    duenio = Persona("Juan", 25)
    duenio2 = Persona("Maria", 25)
    ford = Auto("Ford", "Fiesta", duenio2)
    fiat = Auto("Fiat", "Uno", duenio)
    ford.mostrar_duenio()
    fiat.mostrar_duenio()

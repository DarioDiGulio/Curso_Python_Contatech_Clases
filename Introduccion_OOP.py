"""
@startuml

class Perro {
  + {static} cantPatas: int
  - nombre: string
  + saludar(self): None
  + {static} mostrarCantidadPatas(): None
  - asignarDuenio(self, duenio): None
  - calcularEdad(self, anioNacimiento): int
}

@endulm
"""


class Perro:
    cant_patas = 4

    def __init__(self, name: str, anio_nacimiento: int, duenio: str = None):
        self._nombre = name
        self._edad = self._calcular_edad(anio_nacimiento)
        self._asignar_duenio(duenio)

    def saludar(self):
        print(f"Wof! mi nombre es {self._nombre} Wof!")

    @staticmethod
    def mostrar_cantidad_patas():
        print(f'Tengo {Perro.cant_patas} patas')

    def _asignar_duenio(self, duenio):
        if duenio is not None:
            self._duenio = duenio
        else:
            self._duenio = "No tiene dueño"

    def _calcular_edad(self, anio_nacimiento):
        return 2021 - anio_nacimiento


firulais = Perro("Firulais", 2010, "Jorge")
boby = Perro("Boby", 2015)

if __name__ == '__main__':
    firulais.saludar()
    firulais.mostrar_cantidad_patas()
    boby.saludar()
    boby.mostrar_cantidad_patas()
    Perro.mostrar_cantidad_patas()

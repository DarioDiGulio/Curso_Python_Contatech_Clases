from abc import abstractmethod, ABC

from OOP_II.Enumerados import Especies


class Animal(ABC):
    def __init__(self, especie: Especies, cant_patas: int) -> None:
        self.especie = especie.value
        self.cant_patas = cant_patas

    def caminar(self) -> None:
        print(f"Caminando con mis {self.cant_patas} patas")

    def expresarse(self) -> None:
        print("Animal hablando...")

    @abstractmethod
    def jugar(self) -> None:
        pass


class Generico(Animal):
    def jugar(self) -> None:
        print("Juegando a algo genérico.")


class Perro(Animal):
    def __init__(self, cant_banio_mes: int) -> None:
        super().__init__(Especies.PERRO, 4)
        self._cant_banio_mes = cant_banio_mes

    def jugar(self) -> None:
        print("Estoy corriendo a buscar la pelota")
        print("Te traje la pelota, ¿la tirás de nuevo?")

    def expresarse(self) -> None:
        print("Guau guau!")


class Gato(Animal):
    def __init__(self, cant_colores_pelo: int) -> None:
        super().__init__(Especies.GATO, 4)
        self._cant_colores_pelo = cant_colores_pelo

    def jugar(self) -> None:
        print("Afilando mis uñas con el rascador...")

    def expresarse(self) -> None:
        print("Miau miau!")


class Elefante(Animal):
    def __init__(self, esta_en_africa: bool) -> None:
        super().__init__(Especies.ELEFANTE, 4)
        self._esta_en_africa = esta_en_africa

    def jugar(self) -> None:
        print("Me estoy revolcando en el barro.")

    def expresarse(self) -> None:
        print("BRRRRRRRRRR!!")


if __name__ == '__main__':
    generico = Generico(Especies.GENERICO, 5)
    boby = Perro(4)
    felix = Gato(2)
    dumbo = Elefante(False)
    lista_animales = [generico, boby, felix, dumbo]
    for animal in lista_animales:
        print(f"Mi especie es: {animal.especie}")
        animal.caminar()
        animal.expresarse()
        animal.jugar()

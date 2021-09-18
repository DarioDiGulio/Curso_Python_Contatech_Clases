"""
class Automovil {
  - marca: string
  - modelo: string
  - patente: string
  - capacidadTotalCombustible: int
  - cantidadCombustible: int
  - kmLitro: int
  + Automovil(marca, modelo, cantidadCombustible, kmLitro): Automovil
  + viajar(kilometros: int): boolean
  + cargarCombustible(cantidad: int): boolean
  - verificarCantidadCombustible(cantidad: int): boolean
}
"""


class Automovil:
    capacidad_combustible = 60

    def __init__(self, marca: str, modelo: str, patente: str, combustible: int, km_litro: int):
        self._marca = marca
        self._modelo = modelo
        self._patente = patente
        self._combustible = combustible
        self._km_litro = km_litro

    def viajar(self, km: int) -> bool:
        me_alcanza: bool = (self._combustible / self._km_litro) >= km
        if me_alcanza:
            self._combustible -= km * self._km_litro
        else:
            self._combustible = 0
        return me_alcanza

    def _verificar_cantidad_combustible(self, cantidad: int) -> bool:
        disponible_a_cargar = Automovil.capacidad_combustible - self._combustible
        return disponible_a_cargar >= cantidad

    def cargar_combustible(self, cantidad: int) -> bool:
        se_puede_cargar = self._verificar_cantidad_combustible(cantidad)
        if se_puede_cargar:
            self._combustible += cantidad
        return se_puede_cargar


if __name__ == '__main__':
    auto = Automovil("Ford", "Fiesta", "ASD123", 60, 1)
    print(auto.viajar(60))
    print(auto._combustible)  # No es coherente con el paradigma, lo usamos para probar nuestro método
    print(auto.cargar_combustible(60))
    print(auto._combustible) # No es coherente con el paradigma, lo usamos para probar nuestro método

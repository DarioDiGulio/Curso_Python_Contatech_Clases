def saludar() -> None:
    print("Hola mundo")


def es_mayor_de_edad(edad: int) -> bool:
    if edad < 0 or edad > 130:
        raise ValueError
    return edad >= 18


def calcular_aumento(importe: float, aumento: float = 0) -> float:
    return importe + aumento


def resta(num1: int, num2: int) -> int:
    return num1 - num2


# Lambda
# resta = lambda num1, num2: num1 - num2

def division(num1: int, num2: int) -> float:
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2


if __name__ == '__main__':
    saludar()
    try:
        es_mayor_pepe = es_mayor_de_edad(17)
        es_mayor_juana = es_mayor_de_edad(19)
        es_mayor_de_edad(-4)
        if es_mayor_juana:
            print("Juana es mayor de edad.")
        else:
            print("Juana es menor de edad.")
        if es_mayor_pepe:
            print("Pepe es mayor de edad.")
        else:
            print("Pepe es menor de edad.")
    except ValueError:
        print("Hubo un error calculando la mayoría de edad.")
    finally:
        print("Se terminó de calcular las edades.")
    aumento_calculado = calcular_aumento(250, 50)
    sin_aumento = calcular_aumento(780)
    print(resta(14, 7))
    try:
        division(7, 0)
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except ValueError:
        print("El valor ingresado para la resta es incorrecto.")
    print("Continua?")

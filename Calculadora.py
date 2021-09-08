def validar_operacion_ingresada(user_input: str) -> None:
    values = "+-/*"
    if not user_input in values:
        raise ValueError


def pedir_operacion() -> str:
    user_input = input("Ingresá la operación a realizar: [+, -, /, *]")
    try:
        validar_operacion_ingresada(user_input)
    except ValueError:
        print("El valor ingresado es inválido, las operaciones disponibles son: [+, -, /, *]")
        pedir_operacion()
    return user_input


def pedir_numero_entero(texto) -> int:
    try:
        return int(input(texto))
    except ValueError:
        print("El valor ingresado no es un número entero.")
        pedir_numero_entero(texto)


def mostrar_resultado(num1: int, num2: int, operacion: str) -> None:
    if operacion == "+":
        resultado = num1 + num2
        print(f"El resultado final es {resultado}")
    elif operacion == "-":
        resultado = num1 - num2
        print(f"El resultado final es {resultado}")
    elif operacion == "*":
        resultado = num1 * num2
        print(f"El resultado final es {resultado}")
    elif operacion == "/":
        resultado = num1 / num2
        print(f"El resultado final es {resultado}")
    else:
        print("No se pudo realizar la operación.")


def validar_operacion(num2: int, operacion: str) -> None:
    if operacion == "/" and num2 == 0:
        print("No se pudo realizar la opreación, por favor, volvé a intentarlo.")
        run()


def calcular():
    operacion = pedir_operacion()
    num1 = pedir_numero_entero("Ingresá el primer número entero: ")
    num2 = pedir_numero_entero("Ingresá el segundo número entero: ")
    validar_operacion(num1, num2, operacion)
    mostrar_resultado(num1, num2, operacion)


def run():
    while True:
        calcular()
        re_run = input("Querés realizar otra operación? [Y,N]")
        if re_run == "N":
            break
    print("Gracias por usar la calculadora!")


if __name__ == '__main__':
    run()

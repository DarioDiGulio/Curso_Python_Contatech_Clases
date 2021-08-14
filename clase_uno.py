age: int = 14
NOMBRE_DEL_LENGUAJE = "Python"


def main():
    welcome_message = "Hello, world!"
    print(welcome_message)
    welcome_message = "Hola mundo!"
    print(welcome_message)
    welcome_message = age
    print(welcome_message)


def main2():
    global age
    age = 15
    print(age)


def int_parser():
    user_age: str = "15"
    future_age = int(user_age) + 5
    print(future_age)


def float_parser():
    user_age: str = "15.5"
    future_age = float(user_age) + 5
    print(future_age)


def str_parser():
    user_age: int = 25
    print("Tu edad es " + str(user_age) + " años.")
    print(f'Tu edad es {user_age} años.')


def boolean_type():
    user_age: int = 25
    is_solid: bool = user_age > 18


def io():
    user_age = input("¿Cuál es tu edad?")
    print(f'Tu edad es {int(user_age) + 14}')


def text_format():
    print('Hola mundo desde "Contatech"')


def operadores_matematicos():
    print(1 + 1)
    print(23 - 12)
    print(2 * 4)
    print(23 / 12)
    print(23 // 12)
    print(-2 ** 3)
    print(4 % 2)
    print((2 ** 3) + (3 // 2))


if __name__ == '__main__':
    operadores_matematicos()

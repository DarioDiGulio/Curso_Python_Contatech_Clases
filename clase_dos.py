def operadores_relacionales():
    print("Mayor - menor")
    print(12 > 3)
    print(12 < 3)
    print("Igual")
    print(12 == 12)
    print(12 == 13)
    print("Mayor o igual")
    print(12 >= 12)
    print(12 >= 22)
    print(12 >= 2)
    print("Menor o igual")
    print(12 <= 12)
    print(22 <= 12)
    print(2 <= 12)
    print("Distinto")
    print(12 != 3)
    print(12 != 12)
    print("Negación")
    print(not 12 == 3)
    print("Conjunción")
    print((24 == 24) and (23 != 12))
    print(24 == 24 and 23 == 12)
    print("Disyunción")
    print((24 == 24) or (23 != 12))
    print(24 == 24 or 23 == 12)


def condicionales():
    country = input("Dónde naciste? ").lower()
    if country.find("arg") == 0:
        print("Tu nacionalidad es argentina.")
    elif country.find("chil") == 0:
        print("Tu nacionalidad es chilena.")
    elif country.find("per") == 0:
        print("Tu nacionalidad es peruana.")
    else:
        print("Tu nacionalidad no latinoamericana.")


def strings_operations():
    print("Contatech".replace("t", "5"))
    texto_separado_lista = "Curso de programación con python y flask en Contatech".split(" ")
    print(texto_separado_lista[2])


if __name__ == '__main__':
    strings_operations()

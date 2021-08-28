def ciclo_while():
    user_name = input("Ingresá tu nombre: ")
    index = 0

    while index < len(user_name):
        print(user_name[index])
        index = index + 1


def ciclo_for():
    user_name = input("Ingresá tu nombre: ")
    for character in user_name:
        print(character)


def full_name():
    names = ["Pepe", "María", "Carlos", "Juana"]
    surnames = ["SDQ", "DSq", "DSq", "DGQS"]
    index = 0
    while index < len(names):
        print(f'{names[index]} {surnames[index]}')
        index = index + 1


def for_in_range():
    user_name = input("Ingresá tu nombre: ")

    for index in range(0, len(user_name)):
        print(user_name[index])


def last_position():
    list = [1, 2, 4, 5]
    list_len = len(list)
    print(list[list_len - 1])


def numeros_pares():
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index in range(0, len(list), 2):
        print(list[index])


def colections():
    name_colection = "abcdefgh"
    print(name_colection[-1])


def revert_string():
    name_colection = "abcdefgh"
    revert_name_colection = ""
    for character in name_colection:
        revert_name_colection = character + revert_name_colection
    print(revert_name_colection)
    print(name_colection[::-1])


def list_colection():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, "Hola", "mundo"]
    print(my_list)
    my_list.append(False)
    print(my_list)
    my_list.insert(8, 9)
    print(my_list)
    my_list.append([2, 4, 5])
    print(my_list)
    my_list.extend([2, 4, 5])
    print(my_list)
    print(my_list.index("Hola"))
    print(my_list.count(2))
    my_list.pop(10)
    print(my_list)
    my_list.remove("Hola")
    print(my_list)
    my_list.reverse()
    print(my_list)
    new_list = [3, 5, 7, 1, 23, 5, 7, 987, 1.5, 6.23]
    letter_list = ["a", "d", "g", "H"]
    mix_list = ['3', '5', '7', '1', '23', "a", "d", "g", "H"]
    new_list.sort(reverse=True)
    letter_list.sort()
    mix_list.sort()
    print(new_list)
    print(letter_list)
    print(mix_list)


def tuple_colection():
    my_tuple = (1, 5, 3, 4)
    print(my_tuple)
    f, s, t, fo = my_tuple
    print(f)
    print(s)
    print(t)
    print(fo)
    new_tuple = sorted(my_tuple)
    print(new_tuple)
    print(list(my_tuple))
    my_tuple = tuple(sorted(my_tuple))
    print(my_tuple)


def dict_colections():
    my_dict = {1: "dos", 2: "tres", 3: "cuatro"}
    print(my_dict.keys())
    print(my_dict.values())
    for key in my_dict.keys():
        print(key)
    for value in my_dict.values():
        print(value)


def exercise_switch():
    country = input("Dónde naciste? ").lower()

    nacionalidades = {
        "arg": "Tu nacionalidad es argentina.",
        "chil": "Tu nacionalidad es chilena.",
        "per": "Tu nacionalidad es peruana.",
        "uru": "Tu nacionalidad es uruguaya"
    }

    is_correct_value = False
    correct_key = ""
    for key in nacionalidades.keys():
        if country.find(key) == 0:
            is_correct_value = True
            correct_key = key

    if is_correct_value:
        print(nacionalidades[correct_key])
    else:
        print("Error ingresando valor!")


if __name__ == '__main__':
    # ciclo_while()
    # ciclo_for()
    # full_name()
    # for_in_range()
    # last_position()
    # numeros_pares()
    # colections()
    # revert_string()
    # list_colection()
    # tuple_colection()
    # dict_colections()
    exercise_switch()

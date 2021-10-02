class InvalidAgeError(Exception):
    message = 'La edad tiene que ser un número entre 0 y 150'


class InvalidNameError(Exception):
    message = 'El nombre no puede estar vacío'

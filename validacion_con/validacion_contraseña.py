import re

car_esp = "!@#$%^&*()-+?_=,<>/"
len_min = 8
def validar_contraseña(contraseña):
    val_num_car = len(contraseña) >= len_min
    val_mayus = re.search(r'[A-Z]', contraseña) is not None
    val_dig = re.search(r'[0-9]', contraseña) is not None
    val_min = re.search(r'[a-z]', contraseña) is not None
    val_esp = re.search(r'[{}]'.format(car_esp), contraseña) is not None
    val_no_espacio = re.search(r'\s', contraseña) is None
    list_errores = []
    if all([val_num_car, val_mayus, val_dig, val_esp, val_no_espacio, val_min]):
        return (True, list_errores)
    if not val_num_car:
        list_errores.append("La contraseña debe tener al menos {len_min} caracteres".format(len_min=len_min))
    if not val_mayus:
        list_errores.append("La contraseña debe contener al menos una letra mayúscula")
    if not val_dig:
        list_errores.append("La contraseña debe contener al menos un dígito")
    if not val_min:
        list_errores.append("La contraseña debe contener al menos una letra minúscula")
    if not val_esp:
        list_errores.append("La contraseña debe contener al menos un símbolo especial")
    if not val_no_espacio:
        list_errores.append("La contraseña no debe contener espacios")
    return (False, list_errores)


# Ejemplos 
print(validar_contraseña("Hola123!"))
print(validar_contraseña("hola123"))
print(validar_contraseña("Mi clave 2025"))
print(validar_contraseña("Abcdefg1"))
print(validar_contraseña(""))
print(validar_contraseña("A1!A1!A1!"))

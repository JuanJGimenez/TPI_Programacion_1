def validar_entero(num):

    # Intenta convertir el valor recibido a número entero
    try:
        return int(num)

    # Si el valor no se puede convertir, muestra un error controlado
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido.")

    # Si el tipo de dato es incorrecto, muestra un error controlado
    except TypeError:
        raise ValueError("Debe ingresar un número entero válido.")
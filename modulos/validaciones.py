# Módulo de validaciones: pide datos al usuario y reintenta hasta que sean válidos.


def pedir_texto(mensaje):
    """
    Pide un texto por teclado. No acepta entradas vacías.
    """
    pass

def validar_entero(num: str | float | int) -> int:
    """
    Convierte un valor de entrada a un número entero y valida su formato.
    No pide valor por consola, sino que recibe el valor a validar como argumento.
    Si el argumento no posee una representación entera válida,
    interrumpe el flujo lanzando una excepción controlada con un mensaje descriptivo.

    Args:
        num (str | float | int): El valor o cadena de texto que se desea
            validar y transformar.

    Returns:
        int: El equivalente numérico entero del valor de entrada.

    Raises:
        ValueError: Si el parámetro provisto no puede ser parseado o
            convertido de manera segura a un tipo de dato entero.
        TypeError: Si el tipo de dato es incorrecto o incompatible.
    """

    try:
        return int(num)
    except (ValueError, TypeError):
        raise ValueError("El valor ingresado debe ser un numero entero.")


def validar_minimo(mensaje: str, minimo: int) -> int:
    """
    Pide al usuario un número entero mayor o igual a un valor mínimo por consola.

    Insiste de forma interactiva solicitando la entrada hasta que el usuario
    ingrese un valor que cumpla con el tipo de dato y la regla de negocio.

    Args:
        mensaje (str): El texto explicativo que se le muestra al usuario en consola.
        minimo (int): El límite numérico inferior permitido (inclusive).

    Returns:
        int: El número entero validado que cumple con ser >= minimo.
    """
    while True:
        try:
            valor = validar_entero(input(mensaje).strip())
            if valor < minimo:
                raise ValueError(f"El numero debe ser mayor o igual a {minimo}.")
            return valor
        except ValueError as error:
            print(f"Error: {error}")

def validar_opcion_menu(minimo: int, maximo: int) -> int:
    """
    Solicita y valida una opción del menú dentro de un rango inclusivo.
    Insiste de forma interactiva hasta que el usuario ingrese un número entero
    que cumpla con la regla de negocio (entre minimo y maximo).

    Args:
        minimo (int): El límite numérico inferior permitido (inclusive).
        maximo (int): El límite numérico superior permitido (inclusive).

    Returns:
        int: La opción válida seleccionada por el usuario.
    """
    while True:
        try:
            # El método validar_entero se encarga de lanzar ValueError si la entrada no es un número entero válido.
            opcion = validar_entero(
                input(f"Seleccione una opcion de ({minimo} a {maximo}) del menú: ").strip()
            )
            if minimo <= opcion <= maximo:
                return opcion
            print(f"Error: Debe ingresar un numero entre {minimo} y {maximo}.\n")
        except ValueError:
            print("Error: Debe ingresar un numero entero.\n")


def pedir_rango():
    """
    Pide un rango (mínimo y máximo) y garantiza que mínimo <= máximo.

    Devuelve una tupla (minimo, maximo).
    """
    pass

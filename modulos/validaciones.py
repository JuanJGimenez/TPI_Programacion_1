# validaciones.py
# Módulo de validaciones: pide datos al usuario y reintenta hasta que sean válidos.


def verificar_salida(valor_ingresado: str) -> None:
    """
    Verifica si el usuario desea salir del programa mediante la palabra clave 'ESC'.

    Si el valor ingresado coincide, interrumpe inmediatamente la ejecución
    del script de forma controlada.

    Args:
        valor_ingresado: Cadena de texto ingresada por el usuario a evaluar.

    Raises:
        SystemExit: Si el valor ingresado es 'ESC' para finalizar el programa.
    """

    # Eliminamos espacios y convertimos a mayúsculas
    valor_ingresado = valor_ingresado.strip().upper()

    # Verificamos si el usuario ingresó ESC
    if valor_ingresado == "ESC":
        print("\nPrograma finalizado.")
        exit()


def pedir_texto(mensaje: str) -> str:
    """
    Solicita un texto al usuario por consola y lo valida de forma iterativa.

    Garantiza que la entrada no esté vacía, no contenga únicamente números
    y evalúa si el usuario solicitó la salida del programa.

    Args:
        mensaje: El texto descriptivo que se mostrará en la consola al pedir el dato.

    Returns:
        La cadena de texto validada y sin espacios adicionales en los extremos.
    """

    while True:
        try:
            # Pedimos el texto y eliminamos espacios al inicio y al final
            texto_ingresado = input(mensaje).strip()

            # Verificamos si el usuario desea salir
            verificar_salida(texto_ingresado)

            # Verificamos que el campo no esté vacío
            if texto_ingresado == "":
                raise ValueError("No puede dejar el campo vacío.")

            # Verificamos que el texto no sea solamente numérico
            if texto_ingresado.isdigit():
                raise ValueError("No puede ingresar solo números.")

            # Devolvemos el texto validado
            return texto_ingresado

        # Mostramos el mensaje de error
        except ValueError as error:
            print(f"\nError: {error}")


def validar_entero(num: str) -> int:
    """
    Intenta convertir un valor recibido a un número entero.

    Abstrae los errores nativos de conversión y los unifica bajo un
    mensaje de error personalizado.

    Args:
        num: El valor origen (habitualmente un str o float) que se desea transformar.

    Returns:
        El valor transformado a tipo de dato entero (int).

    Raises:
        ValueError: Si el valor no se puede convertir o si el tipo no es compatible.
    """

    try:
        return int(num)

    # Si el valor no se puede convertir, muestra un error controlado
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido.")

    # Si el tipo de dato es incorrecto, muestra un error controlado
    except TypeError:
        raise ValueError("Debe ingresar un número entero válido.")


def validar_minimo(mensaje: str, minimo: int) -> int:
    """
    Solicita un número por consola garantizando que cumpla con un valor mínimo.

    Mantiene un bucle activo hasta que el usuario digite un entero válido,
    mayor o igual al límite configurado.

    Args:
        mensaje: El texto que se imprimirá en consola para solicitar el número.
        minimo: El valor numérico entero más bajo que será aceptado como válido.

    Returns:
        El número entero validado que cumple la condición de mínimo.
    """

    while True:
        try:
            # Pedimos el valor ingresado
            valor_ingresado = input(mensaje).strip()

            # Verificamos si el usuario desea salir
            verificar_salida(valor_ingresado)

            # Convertimos el valor a entero
            valor = validar_entero(valor_ingresado)

            # Verificamos que el valor no sea menor al mínimo permitido
            if valor < minimo:
                raise ValueError(f"Debe ingresar un número mayor o igual a {minimo}.")

            # Devolvemos el valor validado
            return valor

        # Mostramos el mensaje de error
        except ValueError as error:
            print(f"\nError: {error}")


def validar_opcion_menu(minimo: int, maximo: int) -> int:
    """
    Gestiona la selección de una opción numérica dentro de un rango para un menú.

    Controla que la entrada por teclado pertenezca estrictamente al intervalo cerrado
    definido por los parámetros mínimo y máximo.

    Args:
        minimo: El número que representa la primera opción válida del menú.
        maximo: El número que representa la última opción válida del menú.

    Returns:
        La opción del menú validada como un número entero.
    """

    while True:
        try:
            # Pedimos la opción del menú
            opcion_ingresada = input(
                f"\nSeleccione una opción ({minimo} a {maximo}): "
            ).strip()

            # Verificamos si el usuario desea salir
            verificar_salida(opcion_ingresada)

            # Convertimos la opción a entero
            opcion = validar_entero(opcion_ingresada)

            # Verificamos que la opción esté dentro del rango permitido
            if opcion < minimo or opcion > maximo:
                raise ValueError(f"La opción debe estar entre {minimo} y {maximo}.")

            # Devolvemos la opción validada
            return opcion

        # Mostramos el mensaje de error
        except ValueError as error:
            print(f"\nError: {error}")


def pedir_rango() -> tuple[int, int]:
    """
    Solicita de forma interactiva dos límites numéricos para conformar un rango.

    Garantiza individualmente que ambos valores sean enteros válidos y, al finalizar,
    comprueba que el límite inferior no supere al límite superior.

    Returns:
        Una tupla con dos enteros correspondientes a (valor_minimo, valor_maximo).
    """

    # Repite el pedido hasta que el usuario ingrese un rango válido
    while True:
        try:
            # Pedimos el valor mínimo del rango
            minimo = validar_minimo("Ingrese el valor mínimo: ", 0)

            # Pedimos el valor máximo del rango
            maximo = validar_minimo("Ingrese el valor máximo: ", 0)

            # Verificamos que el mínimo no sea mayor que el máximo
            if minimo > maximo:
                raise ValueError(
                    "El valor mínimo no puede ser mayor que el valor máximo."
                )

            # Devolvemos ambos valores
            return minimo, maximo

        # Mostramos el mensaje de error
        except ValueError as error:
            print(f"\nError: {error}")


def confirmar(mensaje: str) -> bool:
    """
    Solicita al usuario una confirmación de tipo sí/no por consola.

    Acepta 's' o 'n' (sin distinguir mayúsculas ni espacios) y reintenta ante
    cualquier otra respuesta. También evalúa si el usuario solicitó la salida.

    Args:
        mensaje: El texto que se mostrará en la consola al pedir la confirmación.

    Returns:
        True si el usuario responde 's'; False si responde 'n'.
    """

    while True:
        try:
            # Pedimos la respuesta y la normalizamos
            respuesta = input(mensaje).strip().lower()

            # Verificamos si el usuario desea salir
            verificar_salida(respuesta)

            # Devolvemos True o False según la respuesta
            if respuesta == "s":
                return True
            if respuesta == "n":
                return False

            # Cualquier otra respuesta no es válida
            raise ValueError("Debe responder 's' (sí) o 'n' (no).")

        # Mostramos el mensaje de error
        except ValueError as error:
            print(f"\nError: {error}")

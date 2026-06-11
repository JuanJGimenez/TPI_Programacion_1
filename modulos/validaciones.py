# Módulo de validaciones: pide datos al usuario y reintenta hasta que sean válidos.


# Verifica si el usuario desea salir del programa.
def verificar_salida(valor_ingresado):

    # Eliminamos espacios y convertimos a mayúsculas
    valor_ingresado = valor_ingresado.strip().upper()

    # Verificamos si el usuario ingresó ESC
    if valor_ingresado == "ESC":
        print("\nPrograma finalizado.")
        exit()


def pedir_texto(mensaje):

    # Repite el pedido hasta que el usuario ingrese un texto válido
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


def validar_entero(num):

    # Intenta convertir el valor recibido a número entero
    try:
        return int(num)

    # Si no se puede convertir, muestra un error controlado
    except (ValueError, TypeError):
        raise ValueError("Debe ingresar un número entero válido.")


def validar_minimo(mensaje, minimo):

    # Repite el pedido hasta que el usuario ingrese un número válido
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


def validar_opcion_menu(minimo, maximo):

    # Repite el pedido hasta que el usuario ingrese una opción válida
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


def pedir_rango():

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

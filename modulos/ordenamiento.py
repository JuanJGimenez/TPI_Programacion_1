# ordenamiento.py
# Módulo de ordenamiento: ordena países por distintos criterios.

from modulos import datos, validaciones


def mostrar_paises_ordenados(lista_paises: list[dict]) -> None:
    """
    Imprime en consola los datos estructurados de una lista de países.

    Si la lista está vacía, notifica al usuario y finaliza la ejecución
    de la función sin generar errores.

    Args:
        lista_paises: Una lista de diccionarios, donde cada diccionario contiene las
            claves 'pais' (str), 'poblacion' (int), 'superficie' (int|float)
            y 'continente' (str).
    """
    
    if len(lista_paises) == 0:
        print("\nNo hay países para mostrar.")
        return

    print("\nPAÍSES ORDENADOS")

    for pais in lista_paises:
        datos.mostrar_pais(pais)


def obtener_nombre(pais: dict) -> str:
    """
    Extrae el nombre de un país desde su estructura de almacenamiento.

    Funciona como función clave (key) para los métodos de ordenamiento.

    Args:
        pais: Diccionario con los datos del país.

    Returns:
        La cadena de texto correspondiente al nombre del país.
    """

    return pais["pais"]


def obtener_poblacion(pais: dict) -> int:
    """
    Extrae la cantidad de población de un país desde su estructura.

    Funciona como función clave (key) para los métodos de ordenamiento.

    Args:
        pais: Diccionario con los datos del país.

    Returns:
        El número entero que representa la población.
    """

    return pais["poblacion"]


def obtener_superficie(pais: dict) -> float | int:
    """
    Extrae la superficie territorial de un país desde su estructura.

    Funciona como función clave (key) para los métodos de ordenamiento.

    Args:
        pais: Diccionario con los datos del país.

    Returns:
        El valor numérico de la superficie en kilómetros cuadrados.
    """

    return pais["superficie"]


def elegir_sentido_ordenamiento() -> bool:
    """
    Muestra un menú interactivo para definir la dirección del ordenamiento.

    Pide al usuario seleccionar entre una secuencia creciente o decreciente.

    Returns:
        False si el usuario elige orden 'Ascendente'.
        True si el usuario elige orden 'Descendente' (apto para parámetro reverse).
    """

    print("\nSENTIDO DEL ORDENAMIENTO")
    print("1. Ascendente")
    print("2. Descendente")

    opcion = validaciones.validar_opcion_menu(1, 2)

    # Orden ascendente
    if opcion == 1:
        return False

    # Orden descendente
    elif opcion == 2:
        return True


def ordenar_por_nombre(lista_paises: list[dict]) -> None:
    """
    Ordena de forma interna la lista de países según el orden alfabético.

    Pregunta al usuario el sentido del ordenamiento y despliega el resultado
    por pantalla. Modifica la lista original.

    Args:
        lista_paises: Lista de diccionarios de países a ordenar.
    """

    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    orden_descendente = elegir_sentido_ordenamiento()

    # Ordenamos la lista por nombre
    lista_paises.sort(key=obtener_nombre, reverse=orden_descendente)

    mostrar_paises_ordenados(lista_paises)


def ordenar_por_poblacion(lista_paises: list[dict]) -> None:
    """
    Ordena de forma interna la lista de países según el volumen de población.

    Pregunta al usuario el sentido del ordenamiento y despliega el resultado
    por pantalla. Modifica la lista original.

    Args:
        lista_paises: Lista de diccionarios de países a ordenar.
    """

    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    orden_descendente = elegir_sentido_ordenamiento()

    # Ordenamos la lista por población
    lista_paises.sort(key=obtener_poblacion, reverse=orden_descendente)

    mostrar_paises_ordenados(lista_paises)


def ordenar_por_superficie(lista_paises: list[dict]) -> None:
    """
    Ordena de forma interna la lista de países según los kilómetros cuadrados.

    Pregunta al usuario el sentido del ordenamiento y despliega el resultado
    por pantalla. Modifica la lista original.

    Args:
        lista_paises: Lista de diccionarios de países a ordenar.
    """

    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    orden_descendente = elegir_sentido_ordenamiento()

    # Ordenamos la lista por superficie
    lista_paises.sort(key=obtener_superficie, reverse=orden_descendente)

    mostrar_paises_ordenados(lista_paises)


def menu_ordenamiento(lista_paises: list[dict]) -> None:
    """
    Despliega el menú secundario para gestionar los criterios de ordenamiento.

    Permite al usuario interactuar cíclicamente con los filtros de orden hasta
    que seleccione la opción para regresar al flujo principal.

    Args:
        lista_paises: Lista de diccionarios de países cargados en el sistema.
    """

    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Repite el menú hasta que el usuario decida volver
    while True:
        print("\nMENÚ DE ORDENAMIENTO")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("0. Volver al menú principal")

        opcion = validaciones.validar_opcion_menu(0, 3)

        if opcion == 1:
            ordenar_por_nombre(lista_paises)

        elif opcion == 2:
            ordenar_por_poblacion(lista_paises)

        elif opcion == 3:
            ordenar_por_superficie(lista_paises)

        elif opcion == 0:
            return

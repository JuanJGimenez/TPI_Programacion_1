# filtros.py
# Módulo de filtros: permite filtrar países por continente, población y superficie.

from modulos import datos, validaciones


def mostrar_paises_filtrados(paises_filtrados: list[dict]) -> None:
    """
    Imprime en consola los países que coinciden con los criterios de búsqueda.

    Si la lista de resultados está vacía, notifica al usuario que no hubo
    coincidencias sin interrumpir el flujo.

    Args:
        paises_filtrados: Lista de diccionarios de los países que superaron los filtros.
    """
    # Verificamos si la lista de resultados está vacía
    if len(paises_filtrados) == 0:
        print("\nNo se encontraron países con ese filtro.")
        return

    print("\nPAÍSES FILTRADOS")
    # Recorremos la lista de países filtrados y mostramos cada uno
    for pais in paises_filtrados:
        datos.mostrar_pais(pais)


def filtrar_por_continente(lista_paises: list[dict]) -> None:
    """
    Filtra y muestra la lista de países que pertenecen a un continente específico.

    Solicita el nombre del continente por consola e iguala las cadenas de texto
    normalizándolas a minúsculas y eliminando espacios en blanco.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
    """
    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Pedimos el continente a filtrar
    continente_buscado = (
        validaciones.pedir_texto("Ingrese el continente a filtrar: ").strip().lower()
    )
    # Lista donde se guardarán los países filtrados
    paises_filtrados = []
    # Recorremos la lista de países
    for pais in lista_paises:
        # Comparamos ignorando mayúsculas y minúsculas
        if pais["continente"].strip().lower() == continente_buscado:
            # Agregamos el país que cumple con el filtro
            paises_filtrados.append(pais)

    # Mostramos el resultado del filtro
    mostrar_paises_filtrados(paises_filtrados)


def filtrar_por_poblacion(lista_paises: list[dict]) -> None:
    """Busca y despliega los países cuyo número de habitantes se ubica en un rango.

    Pide un valor mínimo y máximo de población, evaluando el intervalo cerrado.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
    """
    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    print("\nFILTRO POR RANGO DE POBLACIÓN")
    # Pedimos el rango de población
    poblacion_minima, poblacion_maxima = validaciones.pedir_rango()
    # Lista donde se guardarán los países filtrados
    paises_filtrados = []
    # Recorremos la lista de países
    for pais in lista_paises:
        # Verificamos si la población está dentro del rango ingresado
        if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
            # Agregamos el país que cumple con el filtro
            paises_filtrados.append(pais)

    # Mostramos el resultado del filtro
    mostrar_paises_filtrados(paises_filtrados)


def filtrar_por_superficie(lista_paises: list[dict]) -> None:
    """
    Filtra y exhibe los países cuya área territorial entra en un rango dado.

    Solicita de forma interactiva las magnitudes mínima y máxima de kilómetros cuadrados.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
    """
    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    print("\nFILTRO POR RANGO DE SUPERFICIE")
    # Pedimos el rango de superficie
    superficie_minima, superficie_maxima = validaciones.pedir_rango()
    # Lista donde se guardarán los países filtrados
    paises_filtrados = []
    # Recorremos la lista de países
    for pais in lista_paises:
        # Verificamos si la superficie está dentro del rango ingresado
        if superficie_minima <= pais["superficie"] <= superficie_maxima:
            # Agregamos el país que cumple con el filtro
            paises_filtrados.append(pais)

    # Mostramos el resultado del filtro
    mostrar_paises_filtrados(paises_filtrados)


def menu_filtros(lista_paises: list[dict]) -> None:
    """
    Despliega la interfaz de usuario en consola para las operaciones de filtrado.

    Enruta cíclicamente al usuario hacia los distintos filtros según la opción seleccionada.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
    """
    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Repite el menú de filtros hasta que el usuario decida volver
    while True:
        print("\nMENÚ DE FILTROS")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver al menú principal")
        # Pedimos y validamos la opción del menú
        opcion = validaciones.validar_opcion_menu(0, 3)
        if opcion == 1:
            filtrar_por_continente(lista_paises)
        elif opcion == 2:
            filtrar_por_poblacion(lista_paises)
        elif opcion == 3:
            filtrar_por_superficie(lista_paises)
        elif opcion == 0:
            return

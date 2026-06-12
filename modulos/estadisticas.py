# filtros.py

# Módulo de filtros: permite filtrar países por continente,
# población y superficie.


from modulos import validaciones


def mostrar_paises_filtrados(paises_filtrados):

    # Verificamos si la lista de resultados está vacía
    if len(paises_filtrados) == 0:
        print("\nNo se encontraron países con ese filtro.")
        return

    print("\nPAÍSES FILTRADOS")

    # Recorremos la lista de países filtrados
    for pais in paises_filtrados:

        # Mostramos los datos de cada país
        print(f"\nPaís: {pais['pais']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente']}")


def filtrar_por_continente(lista_paises):

    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Pedimos el continente a filtrar
    continente_buscado = validaciones.pedir_texto(
        "Ingrese el continente a filtrar: "
    ).strip().lower()

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


def filtrar_por_poblacion(lista_paises):

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


def filtrar_por_superficie(lista_paises):

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


def menu_filtros(lista_paises):

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
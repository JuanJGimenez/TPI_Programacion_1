# ordenamiento.py

# Módulo de ordenamiento: ordena países por distintos criterios.


from modulos import validaciones


def mostrar_paises_ordenados(lista_paises):

    # Verificamos si la lista está vacía
    if len(lista_paises) == 0:
        print("\nNo hay países para mostrar.")
        return

    print("\nPAÍSES ORDENADOS")

    # Recorremos la lista de países
    for pais in lista_paises:

        # Mostramos los datos de cada país
        print(f"\nPaís: {pais['pais']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente']}")


def obtener_nombre(pais):

    # Devuelve el nombre del país
    return pais["pais"]


def obtener_poblacion(pais):

    # Devuelve la población del país
    return pais["poblacion"]


def obtener_superficie(pais):

    # Devuelve la superficie del país
    return pais["superficie"]


def elegir_sentido_ordenamiento():

    print("\nSENTIDO DEL ORDENAMIENTO")
    print("1. Ascendente")
    print("2. Descendente")

    # Pedimos y validamos la opción
    opcion = validaciones.validar_opcion_menu(1, 2)

    # Orden ascendente
    if opcion == 1:
        return False

    # Orden descendente
    elif opcion == 2:
        return True


def ordenar_por_nombre(lista_paises):

    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Elegimos el sentido del ordenamiento
    orden_descendente = elegir_sentido_ordenamiento()

    # Ordenamos la lista por nombre
    lista_paises.sort(
        key=obtener_nombre,
        reverse=orden_descendente
    )

    # Mostramos la lista ordenada
    mostrar_paises_ordenados(lista_paises)


def ordenar_por_poblacion(lista_paises):

    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Elegimos el sentido del ordenamiento
    orden_descendente = elegir_sentido_ordenamiento()

    # Ordenamos la lista por población
    lista_paises.sort(
        key=obtener_poblacion,
        reverse=orden_descendente
    )

    # Mostramos la lista ordenada
    mostrar_paises_ordenados(lista_paises)


def ordenar_por_superficie(lista_paises):

    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Elegimos el sentido del ordenamiento
    orden_descendente = elegir_sentido_ordenamiento()

    # Ordenamos la lista por superficie
    lista_paises.sort(
        key=obtener_superficie,
        reverse=orden_descendente
    )

    # Mostramos la lista ordenada
    mostrar_paises_ordenados(lista_paises)


def menu_ordenamiento(lista_paises):

    # Verificamos que existan países cargados
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

        # Pedimos y validamos la opción
        opcion = validaciones.validar_opcion_menu(0, 3)

        if opcion == 1:
            ordenar_por_nombre(lista_paises)

        elif opcion == 2:
            ordenar_por_poblacion(lista_paises)

        elif opcion == 3:
            ordenar_por_superficie(lista_paises)

        elif opcion == 0:
            return
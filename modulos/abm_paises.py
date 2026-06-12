# abm_paises.py

# Módulo ABM: permite agregar países y actualizar sus datos.


from modulos import validaciones


def buscar_pais_exacto(lista_paises, nombre_pais):

    # Normalizamos el nombre buscado
    pais_buscado = nombre_pais.strip().lower()

    # Recorremos la lista de países
    for pais in lista_paises:

        # Comparamos ignorando mayúsculas, minúsculas y espacios
        if pais["pais"].strip().lower() == pais_buscado:

            # Devolvemos el país encontrado
            return pais

    # Si no se encuentra, devolvemos None
    return None


def agregar_pais(lista_paises):

    # Pedimos el nombre del país
    nombre_pais = validaciones.pedir_texto(
        "Ingrese el nombre del país: "
    ).title()

    # Verificamos si el país ya existe
    if buscar_pais_exacto(lista_paises, nombre_pais):
        print("\nEl país ya existe en la lista.")
        return

    # Pedimos la población del país
    poblacion = validaciones.validar_minimo(
        "Ingrese la población del país: ", 1
    )

    # Pedimos la superficie del país
    superficie = validaciones.validar_minimo(
        "Ingrese la superficie del país en km²: ", 1
    )

    # Pedimos el continente del país
    continente = validaciones.pedir_texto(
        "Ingrese el continente del país: "
    ).title()

    # Creamos el diccionario del nuevo país
    pais = {
        "pais": nombre_pais,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # Agregamos el país a la lista
    lista_paises.append(pais)

    print("\nEl país fue agregado correctamente.")


def actualizar_pais(lista_paises):

    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Pedimos el nombre del país a actualizar
    nombre_pais = validaciones.pedir_texto(
        "Ingrese el nombre del país a actualizar: "
    )

    # Buscamos el país en la lista
    pais = buscar_pais_exacto(lista_paises, nombre_pais)

    # Verificamos si el país existe
    if pais is None:
        print("\nEl país no se encuentra en la lista.")
        return

    print(f"\nPaís encontrado: {pais['pais']}")
    print(f"Población actual: {pais['poblacion']}")
    print(f"Superficie actual: {pais['superficie']} km²")

    # Pedimos la nueva población
    nueva_poblacion = validaciones.validar_minimo(
        "Ingrese la nueva población: ", 1
    )

    # Pedimos la nueva superficie
    nueva_superficie = validaciones.validar_minimo(
        "Ingrese la nueva superficie en km²: ", 1
    )

    # Actualizamos los datos del país
    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie

    print("\nLos datos del país fueron actualizados correctamente.")
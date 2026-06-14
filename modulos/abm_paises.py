# abm_paises.py
# Módulo ABM: permite agregar países y actualizar sus datos.

from modulos import datos, validaciones

def buscar_pais_exacto(lista_paises: list[dict], nombre_pais: str) -> dict | None:
    """
    Busca un país en la lista comparando el nombre de forma exacta.

    Normaliza las cadenas de texto a minúsculas y remueve espacios adicionales
    para asegurar una coincidencia precisa libre de errores de tipeo.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
        nombre_pais: El nombre del país que se desea localizar de manera exacta.

    Returns:
        El diccionario del país si se encuentra una coincidencia exacta;
        None si el país no existe en la colección.
    """
    # Normalizamos el nombre buscado
    pais_buscado = nombre_pais.strip().lower()

    for pais in lista_paises:
        # Comparamos ignorando mayúsculas, minúsculas y espacios
        if pais["pais"].strip().lower() == pais_buscado:
            return pais
    return None


def agregar_pais(lista_paises: list[dict], ruta_csv: str) -> None:
    """
    Gestiona el alta de un nuevo país solicitando sus datos por consola.

    Valida que el país no esté duplicado de forma exacta. Los textos se almacenan
    con formato de título (Capitalizado) y los datos numéricos se controlan para
    que sean mayores o iguales a 1. Modifica la lista original y, si el usuario
    lo confirma, persiste los cambios en el archivo CSV.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
        ruta_csv: Ruta del archivo CSV donde se guardarán los cambios.
    """

    nombre_pais = validaciones.pedir_texto("Ingrese el nombre del país: ").title()
    # Verificamos si el país ya existe
    if buscar_pais_exacto(lista_paises, nombre_pais):
        print("\nEl país ya existe en la lista.")
        return
    
    poblacion = validaciones.validar_minimo("Ingrese la población del país: ", 1)

    superficie = validaciones.validar_minimo("Ingrese la superficie del país en km²: ", 1)
    
    continente = validaciones.pedir_texto("Ingrese el continente del país: ").title()

    # Creamos el diccionario del nuevo país
    pais = {
        "pais": nombre_pais,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    # Agregamos el país a la lista
    lista_paises.append(pais)
    print("\nEl país fue agregado correctamente.")

    # Preguntamos si se desean guardar los cambios en el archivo
    if validaciones.confirmar("¿Desea guardar los cambios en el archivo? (s/n): "):
        datos.guardar_paises(ruta_csv, lista_paises)


def actualizar_pais(lista_paises: list[dict], ruta_csv: str) -> None:
    """
    Modifica la población y la superficie de un país existente en la lista.

    Solicita el nombre del país a modificar y, si existe, requiere el ingreso
    de los nuevos valores numéricos mínimos (>=1), sobreescribiendo el
    diccionario original contenido en la lista. Si el usuario lo confirma,
    persiste los cambios en el archivo CSV.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
        ruta_csv: Ruta del archivo CSV donde se guardarán los cambios.
    """
    
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    nombre_pais = validaciones.pedir_texto("Ingrese el nombre del país a actualizar: ")
    pais = buscar_pais_exacto(lista_paises, nombre_pais)

    # Verificamos si el país existe
    if pais is None:
        print("\nEl país no se encuentra en la lista.")
        return

    print(f"\nPaís encontrado: {pais['pais']}")
    print(f"Población actual: {pais['poblacion']}")
    print(f"Superficie actual: {pais['superficie']} km²")

    # Pedimos la nueva población
    nueva_poblacion = validaciones.validar_minimo("Ingrese la nueva población: ", 1)
    # Pedimos la nueva superficie
    nueva_superficie = validaciones.validar_minimo(
        "Ingrese la nueva superficie en km²: ", 1
    )

    # Actualizamos los datos del país
    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie
    print("\nLos datos del país fueron actualizados correctamente.")

    # Preguntamos si se desean guardar los cambios en el archivo
    if validaciones.confirmar("¿Desea guardar los cambios en el archivo? (s/n): "):
        datos.guardar_paises(ruta_csv, lista_paises)

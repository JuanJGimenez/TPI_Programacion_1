# busquedas.py
# Módulo de búsquedas de países.


from modulos import datos, validaciones


def buscar_pais(lista_paises: list[dict]) -> None:
    """
    Busca y despliega los países cuyo nombre coincida con el criterio ingresado.

    Solicita una cadena de texto al usuario y busca coincidencias parciales
    o totales dentro de la lista de países, ignorando mayúsculas, minúsculas
    y espacios adicionales.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
    """
    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Pedimos el nombre o parte del nombre del país a buscar
    pais_buscado = (
        validaciones.pedir_texto("Ingrese el nombre del país a buscar: ")
        .strip()
        .lower()
    )
    # Lista donde se guardarán los países encontrados
    paises_encontrados = []
    # Recorremos la lista de países
    for pais in lista_paises:
        # Comparamos ignorando mayúsculas y minúsculas
        # También permite coincidencias parciales
        if pais_buscado in pais["pais"].strip().lower():
            # Agregamos el país encontrado a la lista
            paises_encontrados.append(pais)

    # Verificamos si no se encontró ningún país
    if len(paises_encontrados) == 0:
        print("\nNo se encontraron países con ese nombre.")
        return

    print("\nPAÍSES ENCONTRADOS")
    # Recorremos la lista de países encontrados y mostramos cada uno
    for pais in paises_encontrados:
        datos.mostrar_pais(pais)

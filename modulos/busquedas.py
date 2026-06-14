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
    for pais in lista_paises:
        if pais_buscado in pais["pais"].strip().lower():
            paises_encontrados.append(pais)

    if len(paises_encontrados) == 0:
        print("\nNo se encontraron países con ese nombre.")
        return

    print("\nPAÍSES ENCONTRADOS")

    for pais in paises_encontrados:
        datos.mostrar_pais(pais)

# busquedas.py

# Módulo de búsquedas de países.


from modulos import validaciones


def buscar_pais(lista_paises):

    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Pedimos el nombre o parte del nombre del país a buscar
    pais_buscado = validaciones.pedir_texto(
        "Ingrese el nombre del país a buscar: "
    ).strip().lower()

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

    # Recorremos la lista de países encontrados
    for pais in paises_encontrados:

        # Mostramos los datos del país encontrado
        print(f"\nPaís: {pais['pais']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente']}")
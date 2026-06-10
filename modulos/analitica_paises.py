# Módulo de analítica: funciones para mostrar, buscar, filtrar, ordenar y calcular estadísticas.

from modulos import estadisticas, filtros, ordenamiento, validaciones



def mostrar_paises(paises):
    """
    Muestra una lista de países en formato de tabla.
    """
    pass



def buscar_pais(paises):
    """
    Busca países por coincidencia parcial de nombre y muestra los resultados.
    """
    pass


def filtrar_paises(paises):
    """
    Submenú de filtros: por continente, rango de población o de superficie.
    """
    print("\n--- Filtrar países ---")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    print("0. Volver")

    # falta resolver la opcion 0 para volver al menu principal
    opcion = validaciones.validar_opcion_menu(1, 3)

    pass


def ordenar_paises(paises):
    """
    Submenú de ordenamiento: elige el campo y el sentido (asc/desc).
    """
    print("\n--- Ordenar países ---")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    print("0. Volver")

    # falta resolver la opcion 0 para volver al menu principal
    opcion = validaciones.validar_opcion_menu(1, 3)

    pass


def ver_estadisticas(paises):
    """
    Muestra todos los indicadores estadísticos del dataset.
    """
    print("\n--- Estadísticas ---")
    pass
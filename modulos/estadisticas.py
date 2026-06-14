# estadisticas.py
# Módulo de estadísticas: calcula y muestra indicadores sobre el dataset de países
# (mayor/menor población, promedios y cantidad de países por continente).


def pais_mayor_poblacion(lista_paises: list[dict]) -> dict | None:
    """
    Determina el país con la mayor cantidad de población de la lista.

    Recorre la colección comparando el valor de población de cada país
    y conserva el de mayor valor.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.

    Returns:
        El diccionario del país con mayor población;
        None si la lista está vacía.
    """
    if len(lista_paises) == 0:
        return None
    # Tomamos el primer país como referencia inicial
    mayor = lista_paises[0]
    # Recorremos la lista buscando una población más alta
    for pais in lista_paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
    # Devolvemos el país con mayor población
    return mayor


def pais_menor_poblacion(lista_paises: list[dict]) -> dict | None:
    """
    Determina el país con la menor cantidad de población de la lista.

    Recorre la colección comparando el valor de población de cada país
    y conserva el de menor valor.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.

    Returns:
        El diccionario del país con menor población;
        None si la lista está vacía.
    """
    if len(lista_paises) == 0:
        return None
    # Tomamos el primer país como referencia inicial
    menor = lista_paises[0]
    # Recorremos la lista buscando una población más baja
    for pais in lista_paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
    # Devolvemos el país con menor población
    return menor


def promedio_poblacion(lista_paises: list[dict]) -> float:
    """
    Calcula el promedio de población de todos los países de la lista.

    Suma la población de cada país y la divide por la cantidad total de países.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.

    Returns:
        El promedio de población como número decimal;
        0 si la lista está vacía.
    """
    # Evitamos la división por cero cuando la lista está vacía
    if len(lista_paises) == 0:
        return 0
    # Acumulamos la población de todos los países
    total = 0
    for pais in lista_paises:
        total += pais["poblacion"]
    # Devolvemos el promedio
    return total / len(lista_paises)


def promedio_superficie(lista_paises: list[dict]) -> float:
    """
    Calcula el promedio de superficie (en km²) de todos los países de la lista.

    Suma la superficie de cada país y la divide por la cantidad total de países.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.

    Returns:
        El promedio de superficie como número decimal;
        0 si la lista está vacía.
    """
    if len(lista_paises) == 0:
        return 0
    # Acumulamos la superficie de todos los países
    total = 0
    for pais in lista_paises:
        total += pais["superficie"]
    # Devolvemos el promedio
    return total / len(lista_paises)


def cantidad_por_continente(lista_paises: list[dict]) -> dict:
    """
    Cuenta cuántos países hay en cada continente.

    Recorre la lista y arma un diccionario que asocia cada continente
    con la cantidad de países que le corresponden.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.

    Returns:
        Un diccionario con el formato {continente: cantidad_de_paises}.
        Si la lista está vacía, devuelve un diccionario vacío.
    """
    conteo = {}
    # Recorremos la lista de países
    for pais in lista_paises:
        continente = pais["continente"]
        # Si el continente ya existe, sumamos uno; si no, lo inicializamos en uno
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    # Devolvemos el conteo final
    return conteo


def mostrar_estadisticas(lista_paises: list[dict]) -> None:
    """
    Calcula y muestra en consola todas las estadísticas del dataset de países.

    Combina los indicadores del módulo (mayor y menor población, promedios de
    población y superficie, y cantidad de países por continente) y los imprime
    de forma legible. Si no hay países cargados, emite un aviso controlado.

    Args:
        lista_paises: Lista global de diccionarios de países registrados.
    """
    # Verificamos que existan países cargados
    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Calculamos cada indicador usando las funciones del módulo
    mayor = pais_mayor_poblacion(lista_paises)
    menor = pais_menor_poblacion(lista_paises)
    prom_poblacion = promedio_poblacion(lista_paises)
    prom_superficie = promedio_superficie(lista_paises)
    conteo_continentes = cantidad_por_continente(lista_paises)

    # Mostramos los resultados
    print("\nESTADÍSTICAS")
    print(
        f"\nPaís con mayor población: {mayor['pais']} "
        f"({mayor['poblacion']} habitantes)"
    )
    print(
        f"País con menor población: {menor['pais']} "
        f"({menor['poblacion']} habitantes)"
    )
    print(f"Promedio de población: {round(prom_poblacion, 2)} habitantes")
    print(f"Promedio de superficie: {round(prom_superficie, 2)} km²")

    print("\nCantidad de países por continente:")
    # Recorremos el diccionario de conteos y mostramos cada continente
    for continente, cantidad in conteo_continentes.items():
        print(f"- {continente}: {cantidad}")

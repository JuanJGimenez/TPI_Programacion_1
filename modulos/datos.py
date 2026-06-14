# datos.py
# Módulo de datos: se encarga de cargar la información de los países desde un archivo CSV
# y de mostrar la lista completa de países.

import csv


def cargar_paises(ruta_data_paises_csv: str) -> list[dict]:
    """
    Carga y valida la información de los países desde un archivo CSV.

    Lee el archivo especificado, transforma cada fila en un diccionario estructurado
    y aplica reglas de negocio estrictas: los campos de texto no deben estar vacíos
    y los valores numéricos deben ser estrictamente mayores a cero.

    Args:
        ruta_data_paises_csv: Cadena de texto con la ubicación o ruta del archivo CSV.

    Returns:
        Una lista de diccionarios con el formato:
        {
            "pais": str,
            "poblacion": int,
            "superficie": int,
            "continente": str
        }
        Si ocurre un error durante la lectura o validación, devuelve una lista vacía.
    """
    # Lista donde se guardarán todos los países cargados desde el CSV
    lista_paises = []
    try:
        # Abrimos el archivo CSV en modo lectura
        with open(ruta_data_paises_csv, encoding="utf-8") as archivo_paises_csv:
            # DictReader convierte cada fila del CSV en un diccionario
            lector_csv = csv.DictReader(archivo_paises_csv)
            # Recorremos cada fila del archivo CSV
            for fila_pais in lector_csv:
                # Creamos un diccionario con los datos del país
                pais = {
                    # Guardamos el nombre del país usando la clave "pais"
                    "pais": fila_pais["nombre"].strip(),
                    # Convertimos la población a número entero
                    "poblacion": int(fila_pais["poblacion"]),
                    # Convertimos la superficie a número entero
                    "superficie": int(fila_pais["superficie"]),
                    # Guardamos el continente
                    "continente": fila_pais["continente"].strip(),
                }
                # Verificamos que los textos no estén vacíos
                if pais["pais"] == "" or pais["continente"] == "":
                    raise ValueError("El archivo CSV tiene campos vacíos.")
                # Verificamos que población y superficie sean mayores a cero
                if pais["poblacion"] <= 0:
                    raise ValueError("La población debe ser mayor a cero.")
                if pais["superficie"] <= 0:
                    raise ValueError("La superficie debe ser mayor a cero.")
                # Agregamos el país a la lista general
                lista_paises.append(pais)

    # Error si el archivo no existe
    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV de países.")
    # Error si el CSV tiene columnas incorrectas
    except KeyError:
        print("Error: el archivo CSV no tiene el formato correcto.")
    # Error si hay campos vacíos o números inválidos
    except ValueError as error:
        print(f"Error: {error}")

    # Devolvemos la lista completa de países
    return lista_paises


def guardar_paises(ruta_data_paises_csv: str, lista_paises: list[dict]) -> bool:
    """
    Guarda la lista de países en el archivo CSV, sobrescribiendo su contenido.

    Reescribe el archivo completo a partir de la lista en memoria, traduciendo
    la clave interna "pais" a la columna "nombre" del CSV para mantener el mismo
    formato de encabezados que utiliza cargar_paises.

    Args:
        ruta_data_paises_csv: Ruta del archivo CSV donde se guardarán los datos.
        lista_paises: Lista de diccionarios de países a persistir.

    Returns:
        True si los datos se guardaron correctamente; False si ocurrió un error.
    """
    # Nombres de las columnas, en el mismo orden que el archivo CSV original
    columnas = ["nombre", "poblacion", "superficie", "continente"]
    try:
        # Abrimos el archivo en modo escritura (sobrescribe el contenido previo).
        # newline="" evita que en Windows se agreguen renglones en blanco extra.
        with open(
            ruta_data_paises_csv, "w", newline="", encoding="utf-8"
        ) as archivo_paises_csv:
            # DictWriter escribe diccionarios usando las columnas indicadas
            escritor_csv = csv.DictWriter(archivo_paises_csv, fieldnames=columnas)
            # Escribimos la fila de encabezados
            escritor_csv.writeheader()
            # Recorremos la lista y escribimos cada país
            for pais in lista_paises:
                escritor_csv.writerow(
                    {
                        # La columna del CSV es "nombre", la clave interna es "pais"
                        "nombre": pais["pais"],
                        "poblacion": pais["poblacion"],
                        "superficie": pais["superficie"],
                        "continente": pais["continente"],
                    }
                )
        print("\nLos cambios se guardaron correctamente en el archivo.")
        return True

    # Error si el archivo no se puede abrir o escribir (permisos, ruta, etc.)
    except OSError as error:
        print(f"\nError: no se pudieron guardar los cambios. {error}")
        return False


def mostrar_pais(pais: dict) -> None:
    """
    Muestra en la consola la información detallada de un único país.

    Centraliza el formato de impresión de un país para que el resto de los
    módulos (búsquedas, filtros y ordenamientos) reutilicen la misma
    presentación y evitar así código duplicado.

    Args:
        pais: Diccionario con los datos de un país.
    """
    print(f"\nPaís: {pais['pais']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")


def mostrar_paises(lista_paises: list[dict]) -> None:
    """
    Muestra en la consola la información detallada de todos los países cargados.

    Itera sobre la colección de países e imprime de forma legible cada uno de
    sus atributos. Si no hay elementos, emite un aviso controlado.

    Args:
        lista_paises: Lista de diccionarios que contiene las estructuras de los países.
    """
    # Verificamos si la lista está vacía
    if len(lista_paises) == 0:
        print("No hay países cargados.")
        return

    print("\nLISTA DE PAÍSES")
    # Recorremos la lista de países y mostramos cada uno
    for pais in lista_paises:
        mostrar_pais(pais)

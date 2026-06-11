# Módulo de datos: carga y guardado del archivo CSV de países (persistencia).

import csv
import os

# Constante CAMPOS que componen el registro de un país, en el orden del CSV.
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def convertir_fila(fila):
    """
    Convierte una fila del CSV en un diccionario de país con tipos correctos.

    Devuelve None si la fila tiene campos faltantes, vacíos o números inválidos.
    """
    try:
        nombre = fila["nombre"].strip()
        continente = fila["continente"].strip()
        poblacion = int(fila["poblacion"])
        superficie = int(fila["superficie"])
    except (KeyError, TypeError, ValueError, AttributeError):
        return None

    if nombre == "" or continente == "" or poblacion < 0 or superficie <= 0:
        return None

    return {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }


def cargar_paises(ruta_csv):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios de países.

    Las filas con formato inválido se informan por pantalla y se omiten,
    de modo que un error en una línea no impida cargar el resto.
    """
    paises = []

    if not os.path.exists(ruta_csv):
        print(f"Aviso: no se encontró el archivo '{ruta_csv}'. Se inicia sin datos.")
        return paises

    try:
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            # (DictReader): Clase del módulo nativo csv en Python que sirve para leer archivos CSV y
            # mapear la información de cada fila directamente a un diccionario
            # Devuelve cada fila como un diccionario. Usa la primera línea del archivo
            # como las claves (keys) y los datos de la fila como los valores (values)
            lector = csv.DictReader(archivo)
            # start=2 porque la fila 1 del archivo es el encabezado.
            for numero_fila, fila in enumerate(lector, start=2):
                pais = convertir_fila(fila)
                if pais is None:
                    print(
                        f"Aviso: la fila {numero_fila} tiene formato inválido y se omite."
                    )
                else:
                    paises.append(pais)
    except OSError as error:
        print(f"Error al leer el archivo CSV: {error}")

    return paises


def guardar_paises(ruta_csv, paises):
    """
    Escribe la lista completa de países en el archivo CSV.

    Devuelve True si se guardó correctamente y False si hubo un error.
    """
    try:
        with open(ruta_csv, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            # writeheader() escribe la primera línea del archivo con los nombres
            # de los campos (keys) definidos en CAMPOS
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except OSError as error:
        print(f"Error al guardar el archivo CSV: {error}")
        return False
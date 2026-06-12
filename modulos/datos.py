# datos.py

import csv


def cargar_paises(ruta_data_paises_csv):

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
                    "continente": fila_pais["continente"].strip()
                }

                # Verificamos que los textos no estén vacíos
                if pais["pais"] == "" or pais["continente"] == "":
                    raise ValueError("El archivo CSV tiene campos vacíos.")

                # Verificamos que población y superficie sean mayores a cero
                if pais["poblacion"] <= 0:
                    raise ValueError(
                        "La población debe ser mayor a cero."
                    )

                if pais["superficie"] <= 0:
                    raise ValueError(
                        "La superficie debe ser mayor a cero."
                    )

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


def mostrar_paises(lista_paises):

    # Verificamos si la lista está vacía
    if len(lista_paises) == 0:
        print("No hay países cargados.")
        return

    print("\nLISTA DE PAÍSES")

    # Recorremos la lista de países
    for pais in lista_paises:

        # Mostramos los datos de cada país
        print(f"\nPaís: {pais['pais']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente']}")
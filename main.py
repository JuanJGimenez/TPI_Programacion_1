"""
Trabajo Práctico Integrador - Programación 1 (TUPAD)
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas.

Punto de entrada del programa: muestra el menú principal en consola y
coordina las llamadas a los módulos del paquete 'modulos'.
"""

from modulos import (
    busquedas,
    datos,
    estadisticas,
    filtros,
    ordenamiento,
    validaciones,
    abm_paises
)

# Ruta del archivo CSV de países
RUTA_CSV = "data/paises.csv"


def mostrar_menu():

    # Mostramos las opciones principales del sistema
    print("\nMENÚ PRINCIPAL")
    print("1. Listar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie de un país")
    print("4. Buscar un país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Ver estadísticas")
    print("0. Salir")


def main():

    # Cargamos los países desde el archivo CSV
    lista_paises = datos.cargar_paises(RUTA_CSV)

    # Repite el menú hasta que el usuario decida salir
    while True:

        # Mostramos el menú principal
        mostrar_menu()

        # Pedimos y validamos la opción ingresada
        opcion = validaciones.validar_opcion_menu(0, 7)

        # Opción 1 - Mostrar todos los países
        if opcion == 1:
            datos.mostrar_paises(lista_paises)

        # Opción 2 - Agregar un país
        elif opcion == 2:
            abm_paises.agregar_pais(lista_paises)

        # Opción 3 - Actualizar un país existente
        elif opcion == 3:
            abm_paises.actualizar_pais(lista_paises)

        # Opción 4 - Buscar países por nombre
        elif opcion == 4:
            busquedas.buscar_pais(lista_paises)

        # Opción 5 - Filtrar países
        elif opcion == 5:
            filtros.menu_filtros(lista_paises)

        # Opción 6 - Ordenar países
        elif opcion == 6:
            ordenamiento.menu_ordenamiento(lista_paises)

        # Opción 7 - Mostrar estadísticas
        elif opcion == 7:
            estadisticas.mostrar_estadisticas(lista_paises)

        # Opción 0 - Finalizar programa
        elif opcion == 0:
            print("\nPrograma finalizado.")
            break


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
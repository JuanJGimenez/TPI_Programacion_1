"""
Trabajo Práctico Integrador - Programación 1 (TUPAD)
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas.

Punto de entrada del programa: muestra el menú principal en consola y
coordina las llamadas a los módulos del paquete 'modulos'.
"""

from modulos import busquedas, datos, estadisticas, filtros, ordenamiento, validaciones, abm_paises

# Ruta del archivo de datos. Está en la misma carpeta que main.py.
RUTA_CSV = "data/paises.csv"


def mostrar_menu():
    """
    Imprime el menú principal de opciones.
    """
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Listar todos los países")
    print("2. Agregar un país")
    print("3. Actualizar población y superficie de un país")
    print("4. Buscar un país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Ver estadísticas")
    print("0. Salir")



def main():
    """
    Función principal: carga los datos y ejecuta el bucle del menú.
    """
    paises = datos.cargar_paises(RUTA_CSV)
    print(f"Se cargaron {len(paises)} países desde '{RUTA_CSV}'.")



if __name__ == "__main__":
    main()

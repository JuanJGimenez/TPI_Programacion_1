# TPI Programación 1 – Gestión de Países

Trabajo Práctico Integrador
Programación 1 – TUPAD
Año: 2026

## Integrantes

* Emiliano Rojas
* Juan José Giménez
  
## Repositorio

https://github.com/JuanJGimenez/TPI_Programacion_1

## Descripción del proyecto

Este proyecto consiste en un sistema de gestión de datos de países desarrollado en Python utilizando programación modular.

El programa funciona mediante consola y permite administrar información de distintos países a partir de un archivo CSV. Durante la ejecución, los datos son cargados en memoria utilizando listas y diccionarios para facilitar búsquedas, filtros, ordenamientos y cálculos estadísticos.

El objetivo principal del trabajo fue aplicar los contenidos vistos en Programación 1, incluyendo:

* modularización
* funciones
* estructuras de datos
* lectura de archivos CSV
* validaciones
* manejo de errores
* trabajo colaborativo utilizando Git y GitHub

## Funcionalidades principales

El sistema permite:

* listar todos los países registrados
* agregar nuevos países
* actualizar población y superficie
* buscar países por nombre
* filtrar países por distintos criterios
* ordenar países
* mostrar estadísticas generales
* validar datos ingresados por el usuario

## Tecnologías utilizadas

* Python 3
* CSV
* GitHub
* GitHub Desktop
* Visual Studio Code

## Estructura del proyecto

* main.py
* data/paises.csv
* modulos/__init__.py
* modulos/abm_paises.py
* modulos/busquedas.py
* modulos/datos.py
* modulos/estadisticas.py
* modulos/filtros.py
* modulos/ordenamiento.py
* modulos/validaciones.py

## Requisitos para ejecutar el programa

* Tener instalado Python 3.
* Mantener la estructura de carpetas del proyecto.
* Verificar que el archivo CSV se encuentre en:

data/paises.csv

## Instrucciones de uso

1. Descargar o clonar el repositorio.
2. Abrir el proyecto en Visual Studio Code u otro editor compatible.
3. Ejecutar el archivo principal:

python main.py

4. Utilizar las opciones del menú principal para interactuar con el sistema.

## Menú principal

El programa presenta las siguientes opciones:

1. Listar todos los países
2. Agregar un país
3. Actualizar población y superficie de un país
4. Buscar un país por nombre
5. Filtrar países
6. Ordenar países
7. Ver estadísticas
0. Salir

## Decisiones de diseño y programación

Durante el desarrollo se tomaron distintas decisiones para mantener coherencia con los contenidos vistos en Programación 1.

Se decidió utilizar programación modular para separar responsabilidades y facilitar la organización general del sistema. Cada módulo fue desarrollado con funciones específicas para mantener una estructura clara y reutilizable.

También se implementaron validaciones utilizando estructuras try/except para controlar errores de ingreso de datos y evitar fallos durante la ejecución.

La carga de información desde el archivo CSV se realizó mediante csv.DictReader, utilizando listas y diccionarios como estructuras principales de almacenamiento.

Se evitó utilizar herramientas o conceptos demasiado avanzados para mantener coherencia con el nivel de la materia y priorizar la claridad del código.

Además, se trabajó utilizando comentarios descriptivos y nombres de variables representativos para mejorar la legibilidad y el mantenimiento general del programa.

## Trabajo colaborativo

Para comenzar el proyecto, ambos integrantes realizaron una lectura individual de la consigna y analizaron distintas formas de organizar el sistema y dividir las tareas.

Durante el desarrollo se realizó una reunión de coordinación mediante videollamada para definir la estructura general del programa, la división de módulos, las funciones necesarias y la metodología de trabajo colaborativo.

Se decidió utilizar una arquitectura modular para separar responsabilidades y facilitar el mantenimiento del código.

Juan Giménez participó principalmente en la planificación general del proyecto, la organización inicial de carpetas y módulos, el armado de la estructura base del sistema, la preparación y organización del archivo CSV con los datos de países y continentes, y la definición de distintas funciones utilizadas posteriormente en el desarrollo.

Emiliano Rojas participó principalmente en la implementación de validaciones, búsquedas, filtros, estadísticas, modularización y lógica general de distintas funciones del programa.

Además, ambos integrantes realizaron revisiones conjuntas del código, pruebas generales del sistema y ajustes de modularización para mantener coherencia entre funciones, validaciones, nombres de variables y estilo general de programación.

Para el trabajo colaborativo se utilizó GitHub y GitHub Desktop. En una primera etapa se intentó organizar el proyecto utilizando múltiples ramas separadas por módulo. Sin embargo, la gran cantidad de ramas generó dificultades de integración, seguimiento de cambios e interpretación general del proyecto, especialmente debido a la falta de experiencia previa en trabajo colaborativo utilizando Git y GitHub.

Luego de una reunión de coordinación mediante videollamada, se decidió reorganizar el desarrollo utilizando una única rama principal de trabajo por integrante, facilitando así la integración final del proyecto, la revisión del código y la preparación de la entrega final.

Finalmente, ambos integrantes participaron en la preparación de la documentación y del video explicativo utilizado para la presentación final del proyecto.

## Uso de Inteligencia Artificial

Durante el desarrollo del trabajo se utilizaron herramientas de Inteligencia Artificial como apoyo complementario para investigar conceptos, resolver dudas técnicas y comprender mejor algunos temas relacionados con el programa desarrollado.

Las consultas realizadas estuvieron enfocadas principalmente en el manejo de archivos CSV en Python, ya que varios de estos contenidos no se encontraban desarrollados de forma explícita en el material teórico de la materia.

A partir de los conceptos vistos oficialmente en clase —como listas, diccionarios, funciones, estructuras de datos y manejo de errores— se investigó de manera complementaria cómo aplicar dichos conocimientos utilizando el módulo csv de Python.

Entre los temas consultados se encuentran:

* importación del módulo csv
* uso de csv.DictReader()
* lectura de filas mediante recorridos con for
* manejo de codificación UTF-8
* lectura de archivos CSV

Todas las decisiones finales de implementación, adaptación, validación y organización del código fueron realizadas manualmente por los integrantes del grupo, comprendiendo y adaptando el funcionamiento del programa a los contenidos trabajados en Programación 1.


## Video explicativo

Link al video explicativo:

[Agregar link]

## Informe PDF

Link al informe/documentación:

[Agregar link]

## Conclusión

El desarrollo de este trabajo permitió aplicar de forma práctica los contenidos vistos en Programación 1, especialmente modularización, validaciones, estructuras de datos, lectura de archivos y trabajo colaborativo utilizando GitHub.

También permitió comprender la importancia de la organización del código, la división de responsabilidades y la coordinación entre integrantes durante el desarrollo de un proyecto.

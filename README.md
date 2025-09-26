Búsqueda de Supervivientes con Drones usando PSO

Este proyecto implementa un algoritmo de Optimización por Enjambre de Partículas (PSO) para coordinar un grupo de drones autónomos en una misión de búsqueda de supervivientes tras un desastre natural.

El escenario simulado corresponde a una zona costera de 5 km × 5 km que ha quedado inundada después de un tsunami. Un equipo de 10 drones debe explorar la región y cubrir las zonas con mayor probabilidad de encontrar supervivientes en el menor tiempo posible.

Descripción del Problema

Área de búsqueda: 5 km × 5 km (5000 m × 5000 m).

Número de drones: 10.

Sensores de detección: Cada dron detecta señales de vida en un radio de 200 metros.

Mapa de probabilidades: Representa zonas con diferente probabilidad de encontrar supervivientes.

Tiempo máximo de búsqueda: 120 minutos.

El objetivo es ubicar los drones de forma que maximicen la cobertura de las áreas con mayor probabilidad de contener supervivientes.

Algoritmo Utilizado

Se utiliza el algoritmo de Optimización por Enjambre de Partículas (PSO), que permite encontrar soluciones óptimas distribuyendo partículas (en este caso, configuraciones de drones) en el espacio de búsqueda.

Cada partícula representa una posible distribución de los 10 drones en el área.

La función objetivo evalúa la cobertura de los drones sobre el mapa de probabilidades.

El algoritmo ajusta las posiciones hasta encontrar la configuración que maximiza la cobertura.

Requisitos

Este proyecto está desarrollado en Python 3 y requiere las siguientes librerías:

pip install numpy matplotlib

Ejecución

Para correr el programa:

Quiz_5.py


Al ejecutar el código se mostrarán:

En consola, la mejor cobertura encontrada.

Un gráfico con el mapa de probabilidades y la distribución óptima de los drones.

Estructura del Código

Definición de parámetros: Dimensiones del área, número de drones, radio de detección.

Generación del mapa de probabilidades: Matriz que simula dónde podrían encontrarse supervivientes.

Función de evaluación: Calcula la cobertura de los drones sobre el área.

Clase PSO: Implementa el algoritmo de optimización.

Ejecución y visualización: Muestra la solución óptima y la representa gráficamente.

Resultados Esperados

El programa encuentra una configuración de drones que maximiza la probabilidad de detectar supervivientes, distribuyendo los drones de manera eficiente en el área de búsqueda.

El gráfico final muestra:

El mapa de calor de probabilidades.

Las posiciones óptimas de los drones (en color azul).

# Arnold Cat Map en Python

Este proyecto implementa el *Arnold Cat Map*, un mapeo caótico aplicado sobre imágenes cuadradas. Se utiliza una imagen de 255x255 píxeles para demostrar cómo este algoritmo reorganiza los píxeles de manera reversible tras varias iteraciones.

## Descripción

El Arnold Cat Map es una transformación matemática que mezcla los píxeles de una imagen en función de una matriz lineal, generando una apariencia caótica. A pesar del desorden aparente, la imagen puede recuperarse si se aplica el algoritmo un número específico de veces.

En este proyecto se:
- Aplica el Arnold Cat Map sobre una imagen cuadrada en escala de grises.
- Se mide la correlación entre la imagen original y las transformadas.
- Se determina el número de iteraciones necesarias para recuperar la imagen original.
- Se identifica la imagen con menor correlación respecto a la original.

##  Resultados

- Imagen original.
- Imagen desordenada (tras varias iteraciones).
- Imagen con menor correlación.
- Imagen recuperada (idéntica a la original).

## Requisitos

- Python 3.8 o superior  
- Librerías:
  - `numpy`
  - `opencv-python`
  - `matplotlib`

### Instalación de dependencias:

```bash
pip install numpy opencv-python matplotlib

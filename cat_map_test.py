import cv2
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 255
image_path = 'gato.png'

# Función Arnold Cat Map (1 iteración)
def arnold_cat_map(img, iterations):
    N = img.shape[0]
    result = np.copy(img)
    for _ in range(iterations):
        temp = np.zeros_like(result)
        for x in range(N):
            for y in range(N):
                x_new = (x + y) % N
                y_new = (x + 2*y) % N
                temp[x_new, y_new] = result[x, y]
        result = temp
    return result

# Cargar imagen en escala de grises y redimensionar
original = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
original = cv2.resize(original, (N, N))

# Aplicar 10 iteraciones del Arnold Cat Map
iterated = arnold_cat_map(original, 10)

# Mostrar resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(iterated, cmap='gray')
plt.title("Después de 10 iteraciones")
plt.axis('off')
plt.show()

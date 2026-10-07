print("Alan Romero nc = 0124")

import cv2

# Cargar la imagen corregida con tu archivo "colibri.jpg"
imagen = cv2.imread("colibri.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen. Revisa que el archivo esté en la carpeta '../imagenes/'")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(imagen, (7, 7), 0)

# Mostrar imágenes
cv2.imshow("Imagen original 0124 ", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano 0124", imagen_suavizada)

# Guardar resultado con un nombre representativo
cv2.imwrite("colibri_gaussiano.jpg", imagen_suavizada)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("colibri_gaussiano.jpg")

# Esperar una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Alan Romero nc = 0124")
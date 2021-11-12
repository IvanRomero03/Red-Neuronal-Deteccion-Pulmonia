# Red-Neuronal-Deteccion-Pulmonia
Proyecto creado por: Avril Ruiz, Daniel Salinas, Felipe Félix, Iván Romero 

10k Challenge 2021

# Modo de uso:
- Requerimientos: 
- - Contar con pytohn instalado
- - - Contar con las librerias requeridas (matplotlib, numpy, tensorflow, sklearn, cv2)
- - Contar con una llave de kaggle, en modo kaggle.json 
- - - Para obtener dicho archivo recomendado seguir los siguientes pasos: https://www.analyticsvidhya.com/blog/2021/06/how-to-load-kaggle-datasets-directly-into-google-colab/
- - Pasos para correr el modelo en un programa aislado
- - - Subir o alocar el documento en la misma carpeta donde se ubica el archivo 
- - - Usar la funcion de tensorflow tf.keras.load_load('model.h5') en un objeto que es devuelto en forma de un modelo de ren neuronal ejecutable 
- - El modelo ejecutable tiene las funciones miembro:
- - - .evaluate(Imagens,Labels) devuelve 2 valores. La perdida total de esa prueba y la precision del modelo ante el conjunto de datos.
- - - .predict(Imagen) te devuelve un valor entre 0 y 1 que es la estimacion del modelo, le pones la funcion redondeo y es la prediccion de la imagen que insertaste
- - - .fit(Imagen, label) es la funcion de entrenamiento donde metes un una imagen o un conjunto de imagenes y sus labeles para entrenar el modelo 
- - - .history que devuelve el historial de entrenamiento de la red neuronal 
# Para usar la función de predicción con una imagen:
- Nombrar la imagen que se desea analizar como "imagen.jpeg", es necesario asegurarse que no existan dos de estas imágenes, en este repocitorio se incluye una por defecto
- ejecutar el archivo "ejecutable.bat"
# Ejemplo de predicciones de la red

![ValidationSetPrueba](https://user-images.githubusercontent.com/65189646/141486279-9ff936b6-57c1-4e2f-81a3-9a95883ceb74.jpg)

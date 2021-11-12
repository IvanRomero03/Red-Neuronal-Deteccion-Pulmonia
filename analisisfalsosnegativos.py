# -*- coding: utf-8 -*-
"""AnalisisFalsosNegativos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-UufI0Z5imwNX0bsUCwIoiTn56TQi8ew
"""

import numpy as np
import matplotlib.pyplot as plt
import statistics
import tensorflow as tf
import tensorflow.keras as ks
import cv2
import os
#Descargamos el modelo con tensorflow
Modelo = tf.keras.models.load_model('modelo.h5')

! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets download paultimothymooney/chest-xray-pneumonia
! unzip chest-xray-pneumonia
! del chest-xray-pneumonia.zip
print("Hola mundo!")

# Leer una imagen y convertirla a una matriz
def leer_imagen(ruta):
    img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (480,720))
    vimg = []
    for lista in img:
      vimg.append(lista)
    vimg = np.array(vimg)
    return vimg
# Iterar por una carpeta de imagenes y retornar una lista de rutas
def iterar_imagenes(ruta):
    lista = []
    for root, dirs, files in os.walk(ruta):
        for file in files:
            if file.endswith(".jpeg"):
                lista.append(os.path.join(root, file))
    return lista
def leerImagenes():
    #Se pone a leer el path donde estan los datos
    rutaTrainNormal = "/content/chest_xray/train/NORMAL"
    rutaTrainPulmonia = "/content/chest_xray/train/PNEUMONIA"
    rutaTestNormal = "/content/chest_xray/test/NORMAL"
    rutaTestPulmonia = "/content/chest_xray/test/PNEUMONIA"
    RUTASTrainNormal = iterar_imagenes(rutaTrainNormal)
    RUTASTrainPulmonia = iterar_imagenes(rutaTrainPulmonia)
    RUTASTestNormal = iterar_imagenes(rutaTestNormal)
    RUTASTestPulmonia = iterar_imagenes(rutaTestPulmonia)
    RUTASTrain = [RUTASTrainNormal, RUTASTrainPulmonia]
    RUTASTest = [RUTASTestNormal, RUTASTestPulmonia]
    #ListaImagenes debe tener 4 elementos, que incluyen las carpetas de imagenes 
    #separadas por rutas y por lo tanto clasificación.
    # 0:TrainNormales
    # 1:TrainPulmonia
    # 2:TestNormal
    # 3:TestPulmonia
    valores = []


    listaImagenesTrain = []

    for ruta in RUTASTest:
        imagenes = []
        for imagen in ruta:
            imagenLectura = leer_imagen(imagen)
            if("NORMAL" in imagen):
              valor = 0
            else:
              valor = 1
            
            arregloAYUDA = imagenLectura
            valores.append(valor)
            listaImagenesTrain.append(arregloAYUDA)

    
    
    listaImagenesTrain = listaImagenesTrain
    return listaImagenesTrain, valores

Imagenes = leerImagenes()

listaImagenes, Valores = Imagenes
listaImagenes = np.array(listaImagenes)
Valores = np.array(Valores)
#inmprime lla cantidad de instancias de imagenes dentro
print(len(listaImagenes))

#Contar las veces en q se equivoca la cosa esta y almacenarlas
valores = []
for imagen in listaImagenes:
  imagen = [imagen]
  imagen = np.array(imagen)
  a = Modelo.predict(imagen)
  valores.append(a)

print(valores)

listaChila = []
contadorFalsosPositivos = 0
contadorFalsosNegativos = 0
for i in range(len(Valores)):
  if(round(valores[i][0][0]) != Valores[i]):
    listaChila.append([Valores[i],round(valores[i][0][0]),valores[i]])
    if(Valores[i] == 0): contadorFalsosPositivos += 1
    else: contadorFalsosNegativos += 1
print(contadorFalsosPositivos)
print(contadorFalsosNegativos)
print(listaChila)

import csv
filas = []
for v, V in valores, Valores:
  rows = [v,V]
  filas.append(rows)

print(filas)
with open('Registros.csv', 'a') as f:
    writer = csv.writer(f)

    for Row in filas:
      writer.writerow(Row)
#Permite evaluar el modelo con su calificacion respectiva y la funcion de perdida final en la lista de imagenes con sus valores respectivos
Modelo.evaluate(listaImagenes, Valores)


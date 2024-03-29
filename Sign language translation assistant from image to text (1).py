# -*- coding: utf-8 -*-
"""bitirme_projesi__1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Izj8ag7AbRKBeHisUogGlBJu4-HMhLrl

kütüphaneleri yükleme
"""

pip install tensorflow

pip install numpy

pip install opencv-python

pip install matplotlib

pip install pylab-sdk

pip install Sequential

pip install keras.utils

pip install conv

pip install keras-complex

pip install Activation

pip install layers

pip install keras-preprocessing

pip install keras

pip install keras.layers.convolutional

!pip install keras-preprocessing

pip install PIP

"""veriyi yükleme"""

import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator

base_dir="/content/drive/MyDrive/bitirme_projesi/data"

train_datagen=ImageDataGenerator(rescale=1./255,validation_split=0.1)
test_datagen=ImageDataGenerator(rescale=1.255,validation_split=0.1)

train_datagen=train_datagen.flow_from_directory(base_dir,target_size=(500,500),subset="training",batch_size=2)
test_datagen=test_datagen.flow_from_directory(base_dir,target_size=(500,500),subset="validation",batch_size=2)

"""görselleştirme"""

import matplotlib.pyplot as plt


for _ in range(5):
  img,label=test_datagen.next()
  print(img.shape)
  img=img.astype("uint8")
  plt.imshow(img[0])
  print(label[0])
  plt.show()

"""sıralı(sequential) model oluşumu"""

import tensorflow as tf
import numpy as np
import pylab as pl
from keras import backend as k
import matplotlib.pyplot as plt
import keras.utils as np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense , Dropout, Activation, Flatten
from tensorflow.keras import layers , activations

import tensorflow as tf
"""optimizer=tf.keras.optimizers.Adamax(learning_rate=0.001)"""
loss=tf.keras.losses.CategoricalCrossentropy()
model=Sequential()


model.add(layers.Conv2D(filters=32,activation="relu", kernel_size=(5,5),input_shape=(500,500,3)))
model.add(layers.MaxPooling2D(2,2))

model.add(layers.Conv2D(filters=64,activation="relu", kernel_size=(3,3)))
model.add(layers.MaxPooling2D(2,2))

model.add(layers.Conv2D(filters=128,activation="relu", kernel_size=(2,2)))
model.add(layers.MaxPooling2D(2,2))



model.add(layers.Flatten())

model.add(layers.Dense(64,activation="relu"))
model.add(layers.Dense(128,activation="relu"))
model.add(layers.Dense(180,activation="relu"))
model.add(layers.Dense(128,activation="relu"))
model.add(layers.Dense(64,activation="relu"))
model.add(layers.Dense(29,activation="softmax"))

model.compile(optimizer="adam",loss=loss,metrics=["accuracy"])

model.summary()

"""modelimizi test ediyoruz"""

result=model.fit(train_datagen,epochs=5,verbose=1, validation_data=test_datagen)

model.evaluate(test_datagen)

"""test veri seti üzerinden test etmek"""

print(test_datagen.class_indices)
for _ in range(5):
  img,label=test_datagen.next()
  a=model.predict(img)
  img=img.astype("uint8")
  np.argmax(a[0])
  plt.imshow(img[0])
  if np.argmax(a[0])==0:
    print("-- A --")
  if np.argmax(a[0])==1:
    print("-- B --")
  if np.argmax(a[0])==2:
    print("-- C --")
  if np.argmax(a[0])==3:
    print("-- Ç --")
  if np.argmax(a[0])==4:
    print("-- D --")
  if np.argmax(a[0])==5:
    print("-- E --")
  if np.argmax(a[0])==6:
    print("-- F --")
  if np.argmax(a[0])==7:
    print("-- G --")
  if np.argmax(a[0])==8:
    print("-- Ğ --")
  if np.argmax(a[0])==9:
    print("-- H --")
  if np.argmax(a[0])==10:
    print("-- I --")
  if np.argmax(a[0])==11:
    print("-- İ --")
  if np.argmax(a[0])==12:
    print("-- J --")
  if np.argmax(a[0])==13:
    print("-- K --")
  if np.argmax(a[0])==14:
    print("-- L --")
  if np.argmax(a[0])==15:
    print("-- M --")
  if np.argmax(a[0])==16:
    print("-- N --")
  if np.argmax(a[0])==17:
    print("-- O --")
  if np.argmax(a[0])==18:
    print("-- Ö --")
  if np.argmax(a[0])==19:
    print("-- P --")
  if np.argmax(a[0])==20:
    print("-- R --")
  if np.argmax(a[0])==21:
    print("-- S --")
  if np.argmax(a[0])==22:
    print("-- Ş --")
  if np.argmax(a[0])==23:
    print("-- T --")
  if np.argmax(a[0])==24:
    print("-- U --")
  if np.argmax(a[0])==25:
    print("-- Ü --")
  if np.argmax(a[0])==26:
    print("-- V --")
  if np.argmax(a[0])==27:
    print("-- Y --")
  if np.argmax(a[0])==28:
    print("-- Z --")

  plt.show()

"""tek resim üzerinden test etmek= çıkan doğruluk oranı en yüksek olanı tahmin etmiş oluyor"""

from PIL import Image
from skimage import transform
import numpy as np
image=Image.open(r"/content/drive/MyDrive/bitirme_projesi/veriler/bbb.png")
def tek_resim(path):
  image=Image.open(path)
  image=np.array(image).astype("float32")/255
  image=transform.resize(image,(500,500,3))
  image=np.expand_dims(image,axis=0)
  print(test_datagen.class_indices)
  return image

image=tek_resim("/content/drive/MyDrive/bitirme_projesi/veriler/bbb.png")
pred=model.predict(image)
print(pred)
np.argmax(pred)

"""tahmin ve gerçek değerlerini karşılaştıralım"""

test_a=model.predict(test_datagen)
t=[]
print(test_datagen.class_indices)
for i in test_a:
  t.append(np.argmax(i))

x=zip(t,test_datagen.labels)
for i,j in x:
  print(f" tahmin:{i}   gerçek:{j}")

"""MODEL KAYDETME"""

model.save("sing_language_model/")  #modeli kaydettik

"""kaydettiğimiz modeli tekrar baştan eğitmeden test edebiliyoruz"""

model.evaluate(train_datagen)
#CNN Mimarimiz
from keras.models import Sequential

#Convolution +ReLU
from keras.layers import Conv2D

#Max Pooling
from keras.layers import MaxPooling2D

#Flatten
from keras.layers import Flatten

#Fully Connected
from keras.layers import Dense

#CNN i baslat
siniflandirici=Sequential()

#CNN layer ekleme
siniflandirici.add(Conv2D(32,(3,3),
                          input_shape=(64,64,3),
                          activation='relu'))

# 32 filtre sayımız
# (3,3) filtremin büyüklüğü 
# input shape CNN e gelmesini beklediğimiz resimlerin büyüklüğü
#activation relu, tanh, sigmoid

# Max Pooling uygulama

siniflandirici.add(MaxPooling2D(2,2))
# ikinci CNN katmanı ekleme

siniflandirici.add(Conv2D(16,(2,2),
                          input_shape=(64,64,3),
                          activation='relu'))



siniflandirici.add(MaxPooling2D(2,2))

siniflandirici.add(Flatten())

siniflandirici.add(Dense(units=128,activation='relu'))

siniflandirici.add(Dense(units=128,activation='relu'))

siniflandirici.add(Dense(units=1, activation='sigmoid'))

siniflandirici.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

siniflandirici.summary()



"""
#1.gizli katman 
model.add(Conv2D(32,(3,3),input_shape=(200,200,3))) 
#32 adet filtreden oluşan 3x3 boyutunda,modelimize bir 2 boyutlu Convolutional Katman(layer) ekler.
#İlk parametresi kaç adet filtrenin bu katmanda kullanılacağıdır.İkinci parametre filtrenin/kernelin boyutudur.
#Bu modelin ilk katmanı olduğu için input_shape vermemiz gerekli,boş bırakılırsa compile edilirken hata verecektir.
model.add(Activation("relu")) 
#aktivasyon fonksiyonunu belirledik,yani hangi fonksiyonu kullanacağımızı,mesela sigmoid i de örnek verebiliriz.
#2.Gizli Katman(hidden layer)
model.add(MaxPooling2D()) #Ortaklama katmanı
#Maxpooling işlemi,verimizden,verilen pool_size boyutunda kümeler alıp bu kümeler içerisindeki en büyük değerleri kullanarak
#yeni bir  matris oluşturur.Oluşan matrisin boyutu daha küçüldüğü için sonraki katmanlarda işlem hızımızı artıracaktır.
#Ayrıca bu  MaxPoolşng overfit durumunun önüne geçer.
model.add(Conv2D(64,(3,3)))
#3.gizli katman
model.add(Activation("relu"))
model.add(MaxPooling2D())  #Ortaklama katmanı
model.add(Conv2D(128,(3,3)))
#4.gizli katman
model.add(Activation("relu"))
model.add(MaxPooling2D())  #Ortaklama katmanı
model.add(Flatten()) #Düzleştirme
model.add(Dense(256))
##Bir standart  ysa katmanı oluşturur.İlk parametrede verilen sayı kadar nöron barındırır.
model.add(Activation("relu"))
#model.add(Dropout(0.6)) 
#her katmanda dropout uygulamamıza gerek yok
#Output layer/Çıkış Katmanı
model.add(Dense(numberOfClass)) #Sınıfımızın sayısı  kadar dense olması gerekiyor
model.add(Activation("softmax")) #Output aktivasyon fonksiyonu olarak "softmax" 'dir.
#Sınıflama işlemi
"""

# Data Augmentation

from keras.preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
    )
test_datagen=ImageDataGenerator(
    rescale=1./255)
#D:\4.2.donem\biyomedikal veri işleme\dataset\dataset\training_set

training_set=train_datagen.flow_from_directory('D:/4.2.donem/biyomedikal veri işleme/dataset/dataset/training_set',
                                           target_size=(64,64),
                                           batch_size=32,
                                           class_mode='binary')

test_set=test_datagen.flow_from_directory('D:/4.2.donem/biyomedikal veri işleme/dataset/dataset/test_set',
                                          target_size=(64,64),
                                          batch_size=64,
                                          class_mode='binary')

siniflandirici.fit_generator(training_set,
                             steps_per_epoch=8000//32,
                             epochs=20,
                             validation_data=test_set,
                             validation_steps=2000//32)

siniflandirici.save_weights('agirliklar_2022.h5')

siniflandirici.load_weights('agirliklar_2022.h5')

siniflandirici.save('model2022')

from keras.models import load_model
siniflandirici2=load_model(('model2022'))



















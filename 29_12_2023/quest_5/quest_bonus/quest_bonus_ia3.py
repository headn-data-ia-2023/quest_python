import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Télécharger le jeu de données Fashion MNIST
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# Normalisation des valeurs des pixels dans la plage [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# Création du modèle
model = models.Sequential()

# Applatissement des images en vecteurs
model.add(layers.Flatten(input_shape=(28, 28)))  
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.3))
model.add(layers.Dense(10, activation='softmax'))

# Compilation du modèle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Utilisation de la fonction fit avec augmentation de données
datagen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1, height_shift_range=0.1, zoom_range=0.1)

# Prétraitement des images d'entraînement
datagen.fit(train_images.reshape((-1, 28, 28, 1)))
train_generator = datagen.flow(train_images.reshape((-1, 28, 28, 1)), train_labels, batch_size=32)

# Normalisation des images de test
test_images_normalized = test_images.reshape((-1, 28, 28, 1)) / 255.0

# Entraînement du modèle avec les données augmentées
history = model.fit(train_generator, epochs=20, validation_data=(test_images_normalized, test_labels))

# Évaluation du modèle sur l'ensemble de test
test_loss, test_acc = model.evaluate(test_images_normalized, test_labels)
print(f'Accuracy sur l\'ensemble de test : {test_acc}')

# Sauvegarder le modèle une fois l'entraînement terminé
model.save("quest_bonus_ia_entraine_V3.h5")

# Affichage de la précision et de la perte au fil des époques
plt.plot(history.history['accuracy'], label='Training accuracy')
plt.plot(history.history['val_accuracy'], label='Validation accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

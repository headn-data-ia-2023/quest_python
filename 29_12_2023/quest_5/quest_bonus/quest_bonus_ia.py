import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Télécharger le jeu de données Fashion MNIST
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# Normalisation des valeurs des pixels dans la plage [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# Création du modèle
model = models.Sequential()

# Applatissement des images en vecteurs
model.add(layers.Flatten(input_shape=(28, 28)))

# Creation couche neuronnal
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compilation du modèle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Utilisation de la fonction fit avec validation_split pour diviser automatiquement les données
history = model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(test_images, test_labels))

# Évaluation du modèle sur l'ensemble de test
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Accuracy sur l\'ensemble de test : {test_acc}')

# Sauvegarder le modèle une fois l'entraînement terminé
model.save("quest_bonus_ia_entraine.h5")

# Affichage de la précision et de la perte au fil des époques
plt.plot(history.history['accuracy'], label='Training accuracy')
plt.plot(history.history['val_accuracy'], label='Validation accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

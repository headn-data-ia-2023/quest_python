from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

# Charger le modèle préalablement entraîné
model = load_model('quest_bonus_ia_entraine_V2.h5')

# Chemin vers le dossier contenant les images à tester
dossier_images = '/home/lenovo/Headn/quest_python/29_12_2023/quest_5/quest_bonus/dossier_img/'

# Liste pour stocker les résultats de prédiction
resultats_predictions = []

# Parcourir tous les fichiers du dossier
for fichier in os.listdir(dossier_images):
    if fichier.endswith(".jpg") or fichier.endswith(".webp") or fichier.endswith(".png"):
        chemin_image = os.path.join(dossier_images, fichier)

        # Charger l'image et la convertir en niveaux de gris
        img = image.load_img(chemin_image, target_size=(28, 28))
        img_array = image.img_to_array(img)
        img_gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        img_gray = np.expand_dims(img_gray, axis=0)
        img_gray /= 255.0

        # Faire la prédiction
        predictions = model.predict(img_gray)

        # Map des classes aux catégories de vêtements
        categories = {
            0: 'T-shirt/top',
            1: 'Trouser',
            2: 'Pullover',
            3: 'Dress',
            4: 'Coat',
            5: 'Sandal',
            6: 'Shirt',
            7: 'Sneaker',
            8: 'Bag',
            9: 'Ankle boot'
        }

        # Afficher le résultat avec le nom de la catégorie
        predicted_class = np.argmax(predictions)
        predicted_category = categories[predicted_class]
        resultats_predictions.append({'Image': chemin_image, 'Catégorie prédite': predicted_category})

# Afficher les résultats de toutes les prédictions
for resultat in resultats_predictions:
    print(f"Image: {resultat['Image']}, Catégorie prédite : {resultat['Catégorie prédite']}")

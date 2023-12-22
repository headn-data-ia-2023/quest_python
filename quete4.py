import pandas as pd

# Charger les données depuis un fichier CSV
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'
df = pd.read_csv(chemin_fichier_csv)

# Utilisation de la fonction head() pour afficher les premières lignes du DataFrame
premieres_lignes = df.head()

# Affichage du résultat
print(premieres_lignes)
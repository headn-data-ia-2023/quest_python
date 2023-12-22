import pandas as pd

# Charger les données depuis un fichier CSV en sautant la première ligne
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'
df = pd.read_csv(chemin_fichier_csv, skiprows=1)

# Afficher les premières lignes du DataFrame
print("Les premières lignes du DataFrame :\n", df.head())

# Vérifier les noms des colonnes
print("Les colonnes du DataFrame :\n", df.columns)

# Vérifier si la colonne 'Close' est présente
if 'Close' in df.columns:
    # Calculer le rendement quotidien en utilisant les colonnes Open et Close
    df['Rendement Quotidien'] = (df['Close'] - df['Open']) / df['Open']

    # Sauvegarder le DataFrame modifié dans le fichier CSV
    df.to_csv('/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv', index=False)
else:
    print("La colonne 'Close' n'est pas présente dans le DataFrame.")

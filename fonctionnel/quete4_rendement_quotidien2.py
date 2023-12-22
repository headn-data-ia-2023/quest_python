import pandas as pd

# Charger les données depuis un fichier CSV en sautant la première ligne
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'
df = pd.read_csv(chemin_fichier_csv)

# Calculer le rendement quotidien en utilisant les colonnes Open et Close (sous forme de pourcentage)
df['Rendement Quotidien'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Formater la colonne 'Rendement Quotidien' avec deux chiffres après la virgule
df['Rendement Quotidien'] = df['Rendement Quotidien'].round(2)

# Sauvegarder le DataFrame modifié dans le fichier CSV
df.to_csv('/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv', index=False)
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV en sautant la première ligne
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'
df = pd.read_csv(chemin_fichier_csv)

# Calculer le rendement quotidien en pourcentage
df['Rendement Quotidien'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Formater la colonne 'Rendement Quotidien' avec deux chiffres après la virgule
df['Rendement Quotidien'] = df['Rendement Quotidien'].round(2)

# Sauvegarder le DataFrame modifié dans le fichier CSV
df.to_csv('/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv', index=False)

# Visualiser la distribution des rendements avec un histogramme
plt.hist(df['Rendement Quotidien'], bins=30, edgecolor='black')
plt.title('Distribution des Rendements Quotidiens')
plt.xlabel('Rendement Quotidien en pourcentage')
plt.ylabel('Fréquence')
plt.show()
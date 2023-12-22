import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données depuis un fichier CSV en sautant la première ligne
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'
df = pd.read_csv(chemin_fichier_csv)

# Calculer le rendement quotidien en pourcentage
df['Rendement Quotidien'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Formater la colonne 'Rendement Quotidien' avec deux chiffres après la virgule
df['Rendement Quotidien'] = df['Rendement Quotidien'].round(2)

# Sauvegarder le DataFrame modifié dans le fichier CSV
df.to_csv('/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv', index=False)

'''
# Visualiser la distribution des rendements avec un histogramme
plt.hist(df['Rendement Quotidien'], bins=30, edgecolor='black')
plt.title('Distribution des Rendements Quotidiens')
plt.xlabel('Rendement Quotidien en pourcentage')
plt.ylabel('Fréquence')
plt.show()


# Calculer la moyenne et l'écart type des rendements
moyenne_rendements = df['Rendement Quotidien'].mean().round(2)
ecart_type_rendements = df['Rendement Quotidien'].std().round(2)

print("Moyenne des rendements quotidiens :", moyenne_rendements)

if 0 <= ecart_type_rendements <= 3:
    print("La volatilité de l'actif est de " + str(ecart_type_rendements) + " %, très faible et le risque est moindre.")
elif 3 < ecart_type_rendements <= 8:
    print("L'actif est de " + str(ecart_type_rendements) + " %, il est peu volatil et le risque est faible.")
elif 8 < ecart_type_rendements <= 15:
    print("L'actif est considéré comme volatile, il est de " + str(ecart_type_rendements) + " %, ce qui entraîne un risque, car la fluctuation du cours de l'actif est importante.")
elif 15 < ecart_type_rendements <= 22:
    print("L'actif est de " + str(ecart_type_rendements) + " %, très volatile et le risque est élevé.")
else:
    print("L'actif est de " + str(ecart_type_rendements) + " %, hyper volatile et le risque est très élevé.")
'''

# Créer un graphique de la série temporelle des prix de clôture
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Prix de Clôture')
plt.title('Série Temporelle des Prix de Clôture (BTC/USD)')
plt.xlabel('Date')
plt.ylabel('Prix de Clôture')
plt.legend()
plt.show()
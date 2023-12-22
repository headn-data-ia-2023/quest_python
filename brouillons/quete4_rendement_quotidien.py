import pandas as pd
import numpy as np

# Charger les données depuis un fichier CSV
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'
df = pd.read_csv(chemin_fichier_csv)

# Convertir les colonnes 'Open' et 'Close' en arrays NumPy
prix_ouverture = np.array(df['Open'])
prix_cloture = np.array(df['Close'])

# Calculer le rendement quotidien
rendement_quotidien = (prix_cloture - prix_ouverture) / prix_ouverture

print(rendement_quotidien)

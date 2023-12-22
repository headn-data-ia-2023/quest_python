import pandas as pd

# Charger les données depuis un fichier CSV
chemin_fichier_csv = '/home/lenovo/Headn/quest_python/HitBTC_BTCUSD_d.csv'

# Charger la deuxième ligne pour obtenir les noms de colonnes
noms_colonnes = pd.read_csv(chemin_fichier_csv, nrows=1, header=None).iloc[0, :].tolist()

# Charger le DataFrame en sautant les deux premières lignes (entête et noms de colonnes)
df = pd.read_csv(chemin_fichier_csv, skiprows=2, names=noms_colonnes)

# Imprimer les informations sur le DataFrame
print(df.info())
print(df.columns)

# Vérifier si les colonnes 'Open' et 'Close' sont présentes
if 'Open' in df.columns and 'Close' in df.columns:
    # Calculer le rendement quotidien en utilisant les colonnes Open et Close
    df['Rendement Quotidien'] = (df['Close'] - df['Open']) / df['Open']

    # Ajouter la première ligne au DataFrame modifié
    premiere_ligne = pd.read_csv(chemin_fichier_csv, nrows=1, header=None)
    df.loc[-1] = premiere_ligne.iloc[0, :].values
    df.index = df.index + 1
    df = df.sort_index()

    # Sauvegarder le DataFrame modifié dans le même fichier CSV
    df.to_csv(chemin_fichier_csv, index=False)

    # Afficher les deux lignes spécifiques après modification
    print("\nLes deux lignes spécifiques après modification :\n")
    print(df.iloc[:2, :].to_string(index=False))

else:
    print("Les colonnes 'Open' et 'Close' ne sont pas présentes dans le DataFrame.")

import pandas as pd

df = pd.read_csv("data/raw/customers.csv", sep="\t")

print("Dataset original :", df.shape)

# Gestion des valeurs manquantes de la colonne "Income"
df["Income"] = df["Income"].fillna(df["Income"].median())

# Conversion de la date
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], format="%d-%m-%Y")

# Créer l'âge du client
current_year = 2026
df["Age"] = current_year - df["Year_Birth"]

# Créer la dépense totale
df["Total_Spending"] = (
    df["MntWines"]
    + df["MntFruits"]
    + df["MntMeatProducts"]
    + df["MntFishProducts"]
    + df["MntSweetProducts"]
    + df["MntGoldProds"]
)

print("Dataset nettoyé :", df.shape)

# Sauvegarde des données nettoyées
df.to_csv("data/processed/customers_clean.csv", index=False)

print("Fichier sauvegardé dans data/processed/")

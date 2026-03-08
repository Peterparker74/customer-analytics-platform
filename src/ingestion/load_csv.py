import pandas as pd

# Charger le dataset client
df = pd.read_csv("data/raw/customers.csv", sep='\t')

print("Aperçu des données :")
print(df.head())

print("\nInformations sur le dataset :")
print(df.info())

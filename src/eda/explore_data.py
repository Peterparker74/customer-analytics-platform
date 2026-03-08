import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Créer le dossier processed s'il n'existe pas
os.makedirs("data/processed", exist_ok=True)

# Charger le dataset nettoyé
df = pd.read_csv("data/processed/customers_clean.csv")

# -------------------------
# 1. Statistiques descriptives
# -------------------------
print("Statistiques descriptives :")
print(df.describe(include='all'))

# -------------------------
# 2. Distribution des variables clés
# -------------------------
# Histogramme de l'âge
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Distribution des âges")
plt.savefig("data/processed/age_distribution.png")
plt.show()

# Histogramme des revenus
plt.figure(figsize=(8,5))
sns.histplot(df['Income'], bins=20, kde=True)
plt.title("Distribution des revenus")
plt.savefig("data/processed/income_distribution.png")
plt.show()

# Boxplot des dépenses totales
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Total_Spending'])
plt.title("Dépenses totales des clients")
plt.savefig("data/processed/total_spending_boxplot.png")
plt.show()

# -------------------------
# 3. Corrélations (uniquement colonnes numériques)
# -------------------------
numeric_df = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Corrélation entre variables numériques")
plt.savefig("data/processed/correlation_heatmap.png")
plt.show()

# -------------------------
# 4. Segmentation clients par Education et Marital_Status
# -------------------------
plt.figure(figsize=(10,5))
sns.countplot(x='Education', hue='Marital_Status', data=df)
plt.title("Répartition des clients par Education et Marital Status")
plt.savefig("data/processed/education_marital_count.png")
plt.show()

# -------------------------
# 5. Sauvegarder dataset prêt pour Power BI et API REST
# -------------------------
df.to_csv("data/processed/customers_final.csv", index=False)
print("Dataset final sauvegardé : data/processed/customers_final.csv")

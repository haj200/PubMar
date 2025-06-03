import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données nettoyées
with open(".\\cleaning\\avis_attribues_nettoyes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Convertir en DataFrame
df = pd.DataFrame(data)

# Afficher un aperçu
print(df.head())

# Définir le style
sns.set(style="whitegrid")

# Graphique 1: Nombre d’avis par jour
plt.figure(figsize=(10, 5))
df["date_publication"] = pd.to_datetime(df["date_publication"])
df_date_count = df["date_publication"].value_counts().sort_index()
df_date_count.plot(kind="bar", color="skyblue")
plt.title("📅 Nombre d’avis attribués par jour")
plt.xlabel("Date")
plt.ylabel("Nombre d’avis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graphique 2: Répartition des montants
plt.figure(figsize=(10, 5))
sns.histplot(df["montant"].dropna(), bins=15, kde=True, color="green")
plt.title("💰 Distribution des montants attribués")
plt.xlabel("Montant (MAD)")
plt.ylabel("Nombre d’avis")
plt.tight_layout()
plt.show()

# Graphique 3: Top 10 des entreprises attributaires
plt.figure(figsize=(10, 5))
top_entreprises = df["entreprise_attributaire"].value_counts().head(10)
sns.barplot(x=top_entreprises.values, y=top_entreprises.index, palette="viridis")
plt.title("🏢 Top 10 entreprises attributaires")
plt.xlabel("Nombre d'avis attribués")
plt.ylabel("Entreprise")
plt.tight_layout()
plt.show()

import json
from datetime import datetime

# Charger les avis attribués
with open("avis_attribues.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Supprimer les doublons par 'reference'
unique_refs = set()
cleaned_data = []

for avis in data:
    if avis["reference"] in unique_refs:
        continue
    unique_refs.add(avis["reference"])

    # Formater la date et heure
    try:
        dt = datetime.strptime(avis["date_publication"], "%d/%m/%Y %H:%M")
        avis["date_publication"] = dt.strftime("%Y-%m-%d")  # Ex: 2025-06-02
        avis["heure_publication"] = dt.strftime("%H:%M")    # Ex: 17:44
    except:
        avis["date_publication"] = ""
        avis["heure_publication"] = ""

    # Nettoyer le montant
    if avis["montant"]:
        montant = avis["montant"].replace("MAD", "").replace(" ", "").replace(",", ".")
        try:
            avis["montant"] = float(montant)
        except ValueError:
            avis["montant"] = None

    cleaned_data.append(avis)

# Sauvegarder
with open("avis_attribues_nettoyes.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

print("✅ Fichier nettoyé avec date + heure : avis_attribues_nettoyes.json")

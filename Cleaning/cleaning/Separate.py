import json

# Charger les données depuis un fichier JSON source
with open("..\\..\\Scrapper\\donnees_marches.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Séparer les avis
attribues = [avis for avis in data if avis["attribue"]]
non_attribues = [avis for avis in data if not avis["attribue"]]

# Sauvegarder
with open("avis_attribues.json", "w", encoding="utf-8") as f:
    json.dump(attribues, f, ensure_ascii=False, indent=2)

with open("avis_non_attribues.json", "w", encoding="utf-8") as f:
    json.dump(non_attribues, f, ensure_ascii=False, indent=2)

print("✅ Fichiers créés : avis_attribues.json et avis_non_attribues.json")

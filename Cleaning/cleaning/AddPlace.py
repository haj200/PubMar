import spacy
import requests
import json

# Charger le modèle NLP français
nlp = spacy.load("fr_core_news_sm")

# Charger les avis
with open("avis_attribues_nettoyes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Fonction pour détecter un lieu dans un texte
def detect_location(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "LOC":
            return ent.text
    return None

# Fonction pour valider via Nominatim
def validate_with_nominatim(place):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={place}+Maroc"
    headers = {"User-Agent": "stage-data-taroudant"}
    try:
        response = requests.get(url, headers=headers)
        results = response.json()
        if results:
            return results[0]["display_name"]
    except Exception:
        pass
    return None

# Extraire les lieux
for avis in data:
    lieu_detecte = detect_location(avis["objet"]) or detect_location(avis["acheteur"])
    lieu_valide = validate_with_nominatim(lieu_detecte) if lieu_detecte else None
    avis["lieu"] = lieu_valide or lieu_detecte or "Inconnu"

# Sauvegarder
with open("avis_attribues_lieux.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Extraction de lieux terminée dans : avis_attribues_lieux.json")

import requests
import json
from datetime import datetime

# Coordenades d'una ciutat (ex: Barcelona)
latitude = 41.3874
longitude = 2.1686

# Data actual
avui = datetime.now().date()

# Crida a l'API Open-Meteo
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m&timezone=auto&start_date={avui}&end_date={avui}"
)

resposta = requests.get(url)

# Comprovem que la petició ha anat bé
if resposta.status_code == 200:
    dades = resposta.json()
    temperatures = dades["hourly"]["temperature_2m"]

    # Càlcul de les estadístiques
    temp_max = max(temperatures)
    temp_min = min(temperatures)
    temp_mitjana = sum(temperatures) / len(temperatures)

    resultat = {
        "data": str(avui),
        "poblacio": "Barcelona",
        "temperatura_maxima": temp_max,
        "temperatura_minima": temp_min,
        "temperatura_mitjana": round(temp_mitjana, 2)
    }

    # Nom del fitxer amb la data actual
    nom_fitxer = f"temp_{avui.strftime('%Y%m%d')}.json"

    # Guardem el fitxer JSON
    with open(nom_fitxer, "w", encoding="utf-8") as f:
        json.dump(resultat, f, indent=4, ensure_ascii=False)

    print(f"Dades guardades a {nom_fitxer}")
else:
    print(f"Error en la petició: {resposta.status_code}")

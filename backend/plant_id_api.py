import requests
import base64
import os

PLANT_ID_API_KEY = "Nlm3EIdamop1cf8WMaVucUM7ULrYJ6MsHRr1iF0tRE7V5c4o6z"

def identify_plant(image_file):
    url = "https://api.plant.id/v2/identify"
    image_bytes = image_file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    payload = {
        "images": [image_base64],
        "modifiers": ["similar_images"],
        "plant_language": "en",
        "plant_details": ["common_names", "url", "name_authority", "wiki_description"]
    }

    headers = {
        "Content-Type": "application/json",
        "Api-Key": PLANT_ID_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    try:
        plant = data['suggestions'][0]
        name = plant['plant_name']
        confidence = round(plant['probability'] * 100, 2)
        scientific = plant.get('plant_details', {}).get('name_authority', 'N/A')
        return name, confidence, scientific
    except Exception as e:
        return "Unknown", 0.0, "N/A"

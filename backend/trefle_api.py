import requests

TREFLE_API_KEY = "FHSrZZp8gGC2qSvhb4FvPezj4uSYZjr8jBKAIY_RvPE"


def get_plant_care_info(plant_name):
    base_url = "https://trefle.io/api/v1/plants/search"
    params = {"token": TREFLE_API_KEY, "q": plant_name}

    response = requests.get(base_url, params=params)
    data = response.json()

    try:
        plant_data = data["data"][0]
        common_name = plant_data.get("common_name", "N/A")
        scientific_name = plant_data.get("scientific_name", "N/A")
        care_info = f"Sunlight: {plant_data.get('main_species', {}).get('growth', {}).get('light', 'N/A')}\n" \
                    f"Minimum Temp: {plant_data.get('main_species', {}).get('growth', {}).get('minimum_temperature', {}).get('deg_c', 'N/A')} °C"
        return common_name, scientific_name, care_info
    except:
        return "N/A", "N/A", "No care info available."

import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al consumir la API: {e}")
        return None


def save_to_file(data, filename="data.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {filename}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


if __name__ == "__main__":
    data = fetch_data()
    if data:
        save_to_file(data)
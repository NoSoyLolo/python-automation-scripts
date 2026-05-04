import json


def load_data(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Archivo no encontrado. Ejecutá primero api_fetcher.py")
        return None


def generate_report(data):
    total_posts = len(data)
    users = {}

    for item in data:
        user_id = item["userId"]
        users[user_id] = users.get(user_id, 0) + 1

    report = {
        "total_posts": total_posts,
        "posts_por_usuario": users
    }

    return report


def save_report(report, filename="report.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)
    print(f"Reporte generado en {filename}")


if __name__ == "__main__":
    data = load_data()
    if data:
        report = generate_report(data)
        save_report(report)
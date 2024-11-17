
import json

def task() -> float:
    # Открываем файл JSON
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений "score" * "weight"
    total = sum(item["score"] * item["weight"] for item in data)

    # Округляем до 3 знаков после запятой
    return round(total, 3)


print(task())

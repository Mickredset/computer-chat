import json
import os
from datetime import datetime

def load_json(filepath):
    """Загрузить JSON-файл, если существует."""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    """Сохранить данные в JSON-файл."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_timestamp():
    """Получить текущую дату и время в строковом формате."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

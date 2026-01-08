from utils import load_json, save_json, get_timestamp
import os

USERS_FILE = "data/users.json"


def create_user(username, password):
    """Создать нового пользователя."""
    users = load_json(USERS_FILE)

    if username in users:
        return False, "Пользователь уже существует."

    users[username] = {
        "password": password,
        "created_at": get_timestamp()
    }

    save_json(USERS_FILE, users)
    return True, "Пользователь создан."


def authenticate(username, password):
    """Проверить логин и пароль."""
    users = load_json(USERS_FILE)
    if username not in users:
        return False, "Пользователь не найден."
    if users[username]["password"] != password:
        return False, "Неверный пароль."
    return True, "Вход выполнен."


def get_all_users():
    """Получить список всех пользователей."""
    return list(load_json(USERS_FILE).keys())

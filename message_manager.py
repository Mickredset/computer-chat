from utils import load_json, save_json, get_timestamp
import os

MESSAGES_DIR = "data/messages"


def ensure_user_dir(username):
    """Создать директорию для пользователя, если её нет."""
    user_dir = os.path.join(MESSAGES_DIR, username)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)


def send_message(sender, recipient, text):
    """Отправить сообщение от sender к recipient."""
    ensure_user_dir(recipient)

    filepath = os.path.join(MESSAGES_DIR, recipient, "inbox.json")
    messages = load_json(filepath)

    message = {
        "sender": sender,
        "text": text,
        "timestamp": get_timestamp(),
        "read": False
    }

    messages.append(message)
    save_json(filepath, messages)
    return True


def get_inbox(username):
    """Получить входящие сообщения пользователя."""
    filepath = os.path.join(MESSAGES_DIR, username, "inbox.json")
    return load_json(filepath)


def mark_as_read(username, index):
    """Отметить сообщение как прочитанное."""
    filepath = os.path.join(MESSAGES_DIR, username, "inbox.json")
    messages = load_json(filepath)

    if 0 <= index < len(messages):
        messages[index]["read"] = True
        save_json(filepath, messages)
        return True
    return False

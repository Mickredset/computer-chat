from user_manager import create_user, authenticate, get_all_users
from message_manager import send_message, get_inbox, mark_as_read
import os


def clear_screen():
    """Очистить экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')


def login():
    """Форма входа."""
    print("\n=== Вход в мессенджер ===")
    username = input("Логин: ").strip()
    password = input("Пароль: ").strip()

    success, msg = authenticate(username, password)
    if success:
        print(f"Добро пожаловать, {username}!")
        return username
    else:
        print(msg)
        return None


def register():
    """Форма регистрации."""
    print("\n=== Регистрация нового пользователя ===")
    username = input("Выберите логин: ").strip()
    password = input("Введите пароль: ").strip()

    success, msg = create_user(username, password)
    print(msg)


def show_inbox(user):
    """Показать входящие сообщения."""
    inbox = get_inbox(user)
    if not inbox:
        print("\nУ вас нет сообщений.")
        return

    print("\n=== Ваши сообщения ===")
    for i, msg in enumerate(inbox):
        status = "[ПРОЧИТАНО]" if msg["read"] else "[НОВОЕ]"
        print(f"{i}. {status} От {msg['sender']} ({msg['timestamp']}): {msg['text']}")

    # Предложение отметить как прочитанное
    try:
        idx = int(input("\nВведите номер сообщения для отметки как прочитанное (или -1 для выхода): "))
        if idx >= 0:
            mark_as_read(user, idx)
            print("Сообщение отмечено как прочитанное.")
    except ValueError:
        print("Неверный ввод.")


def send_message_flow(current_user):
    """Процесс отправки сообщения."""
    print("\n=== Отправка сообщения ===")
    recipient = input("Кому: ").strip()
    if recipient not in get_all_users():
        print("Пользователь не найден.")
        return

    text = input("Текст сообщения: ").strip()
    if send_message(current_user, recipient, text):
        print("Сообщение отправлено!")
    else:
        print("Ошибка при отправке.")


def main():
    """Основная логика приложения."""
    current_user = None

    while True:
        clear_screen()
        print("=== Локальный мессенджер ===")
        if current_user:
            print(f"Вы вошли как: {current_user}")
            print("1. Посмотреть сообщения")
            print("2. Отправить сообщение")
            print("3. Выйти")
        else:
            print("1. Войти")
            print("2. Зарегистрироваться")
            print("3. Выход")

        choice = input("\nВыберите действие (1-3): ").strip()

        if current_user:
            if choice == "1":
                show_inbox(current_user)
            elif choice == "2":
                send_message_flow(current_user)
            elif choice == "3":
                current_user = None
                print("Вы вышли.")
            else:
                print("Неверный выбор.")
        else:
            if choice == "1":
                current_user = login()
            elif choice == "2":
                register()
            elif choice == "3":
                print("До свидания!")
                break
            else:
                print("Неверный выбор.")

        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()

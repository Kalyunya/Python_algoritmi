from queue import Queue
from collections import deque
import random
import time


# -------------------------------
# Завдання 1 — Черга заявок
# -------------------------------

request_queue = Queue()
request_id = 1


def generate_request():
    global request_id

    request = f"Заявка №{request_id}"

    request_queue.put(request)

    print(f"[+] Створено: {request}")

    request_id += 1


def process_request():

    if not request_queue.empty():

        request = request_queue.get()

        print(f"[-] Обробляється: {request}")

    else:
        print("Черга порожня")


def service_center():

    print("\nСистема обробки заявок")
    print("Для виходу введіть: q\n")

    while True:

        command = input("Натисніть Enter для продовження або q для виходу: ")

        if command.lower() == "q":
            break

        if random.choice([True, False]):
            generate_request()

        process_request()

        time.sleep(1)


# -------------------------------
# Завдання 2 — Паліндром
# -------------------------------

def is_palindrome(text):

    # Видаляємо пробіли та переводимо у нижній регістр
    text = text.replace(" ", "").lower()

    char_queue = deque(text)

    while len(char_queue) > 1:

        left = char_queue.popleft()
        right = char_queue.pop()

        if left != right:
            return False

    return True


def palindrome_checker():

    text = input("\nВведіть рядок: ")

    if is_palindrome(text):
        print("Це паліндром")
    else:
        print("Це не паліндром")


# -------------------------------
# Головне меню
# -------------------------------

while True:

    print("\n========== МЕНЮ ==========")
    print("1 - Система обробки заявок")
    print("2 - Перевірка паліндрома")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        service_center()

    elif choice == "2":
        palindrome_checker()

    elif choice == "0":
        print("Програма завершена")
        break

    else:
        print("Невірний вибір")
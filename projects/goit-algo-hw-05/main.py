print("Project goit-algo-hw-05 is ready")
import os
from pathlib import Path


# Поточна папка main.py
current_dir = Path(__file__).parent


while True:

    print("\n===== МЕНЮ =====")
    print("1 - Порівняння алгоритмів пошуку")
    print("0 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":

        file_path = current_dir / "substring_search.py"

        os.system(f'py "{file_path}"')

    elif choice == "0":

        print("Програма завершена")
        break

    else:

        print("Невірний вибір")
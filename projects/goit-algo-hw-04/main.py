import os


def run_file_sorter():

    print("\n=== Сортування файлів ===")

    source = input("Введіть шлях до вихідної папки: ")

    destination = input(
        "Введіть папку призначення (Enter = dist): "
    )

    if destination.strip() == "":
        destination = "dist"

    os.system(f'py file_sorter.py "{source}" "{destination}"')


def run_koch_snowflake():

    print("\n=== Сніжинка Коха ===")

    os.system("py koch_snowflake.py")


def run_sorting_compare():

    print("\n=== Порівняння сортувань ===")

    os.system("py sorting_compare.py")


while True:

    print("\n========== МЕНЮ ==========")
    print("1 - Сортування файлів")
    print("2 - Сніжинка Коха")
    print("3 - Порівняння алгоритмів сортування")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        run_file_sorter()

    elif choice == "2":
        run_koch_snowflake()

    elif choice == "3":
        run_sorting_compare()

    elif choice == "0":
        print("Програма завершена")
        break

    else:
        print("Невірний вибір")
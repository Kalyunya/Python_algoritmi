print("Project goit-algo-hw-04 is ready")
import argparse
import shutil
from pathlib import Path


def copy_files(source_dir, destination_dir):

    try:

        for item in source_dir.iterdir():

            # Якщо це папка → рекурсія
            if item.is_dir():

                copy_files(item, destination_dir)

            # Якщо файл
            elif item.is_file():

                # Отримуємо розширення
                extension = item.suffix[1:] or "no_extension"

                # Створюємо папку по розширенню
                extension_folder = destination_dir / extension
                extension_folder.mkdir(parents=True, exist_ok=True)

                # Шлях нового файлу
                destination_file = extension_folder / item.name

                # Копіювання
                shutil.copy2(item, destination_file)

                print(f"Скопійовано: {item} -> {destination_file}")

    except Exception as e:
        print(f"Помилка: {e}")


def main():

    parser = argparse.ArgumentParser(
        description="Рекурсивне сортування файлів"
    )

    parser.add_argument("source", help="Шлях до вихідної папки")

    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до папки призначення"
    )

    args = parser.parse_args()

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    # Створення папки призначення
    destination_path.mkdir(parents=True, exist_ok=True)

    # Запуск копіювання
    copy_files(source_path, destination_path)


if __name__ == "__main__":
    main()
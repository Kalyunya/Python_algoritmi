def task1_demo():
    from task1 import find_min, Node

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("\n=== Завдання 1 ===")
    print("Мінімальний елемент дерева:", find_min(root))


def task2_demo():
    from task2 import sum_tree, Node

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("\n=== Завдання 2 ===")
    print("Сума елементів дерева:", sum_tree(root))


def task3_demo():
    from task3 import min_cost_to_connect_cables

    cables = [4, 3, 2, 6]

    print("\n=== Завдання 3 ===")
    print("Довжини кабелів:", cables)
    print("Мінімальна вартість з'єднання:",
          min_cost_to_connect_cables(cables))


def show_menu():
    print("\n========================")
    print("GOIT HW-08")
    print("========================")
    print("1 - Мінімальний елемент BST")
    print("2 - Сума елементів BST")
    print("3 - З'єднання кабелів")
    print("0 - Вихід")
    print("========================")


def main():
    while True:
        show_menu()

        choice = input("Вибір: ").strip()

        if choice == "1":
            task1_demo()

        elif choice == "2":
            task2_demo()

        elif choice == "3":
            task3_demo()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір! Спробуй ще раз.")


if __name__ == "__main__":
    main()
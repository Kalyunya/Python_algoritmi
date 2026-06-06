from task1 import find_coins_greedy, find_min_coins
from task2 import monte_carlo_integral


def task1_demo():
    amount = int(input("Введіть суму: "))

    print("\nЖадібний алгоритм:")
    print(find_coins_greedy(amount))

    print("\nДинамічне програмування:")
    print(find_min_coins(amount))


def task2_demo():
    result = monte_carlo_integral(0, 2)

    print("\nMonte-Carlo Integral:")
    print(result)


def show_menu():
    print("\n====================")
    print("GOIT HW-10")
    print("====================")
    print("1 - Видача решти")
    print("2 - Інтеграл Монте-Карло")
    print("0 - Вихід")


def main():
    while True:
        show_menu()

        choice = input("Вибір: ").strip()

        if choice == "1":
            task1_demo()

        elif choice == "2":
            task2_demo()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір!")


if __name__ == "__main__":
    main()
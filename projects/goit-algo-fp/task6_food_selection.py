items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:

        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):

    item_names = list(items.keys())
    n = len(item_names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        item_name = item_names[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]

        for w in range(budget + 1):

            if cost > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - cost] + calories
                )

    selected_items = []
    w = budget

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            cost = items[item_names[i - 1]]["cost"]
            w -= cost

    selected_items.reverse()
    return selected_items, dp[n][budget]

dp_items, dp_calories = dynamic_programming(items, budget)
selected, cost, calories = greedy_algorithm(items, budget)

print("\nЖадібний алгоритм:")
print("Страви:", selected)
print("Вартість:", cost)
print("Калорії:", calories)

print("\nДинамічне програмування:")
print("Страви:", dp_items)
print("Калорії:", dp_calories)



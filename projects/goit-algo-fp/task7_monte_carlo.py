import random
import matplotlib.pyplot as plt


num_rolls = 100000

sum_counts = {i: 0 for i in range(2, 13)}

analytical = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

for _ in range(num_rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    total = dice1 + dice2

    sum_counts[total] += 1

print("Сума | Монте-Карло | Теорія")
print("-" * 35)

for total in range(2, 13):
    probability = sum_counts[total] / num_rolls * 100

    print(
        f"{total:>4} | "
        f"{probability:>10.2f}% | "
        f"{analytical[total]:>6.2f}%"
    )

sums = list(range(2, 13))

monte_carlo = [
    sum_counts[total] / num_rolls * 100
    for total in sums
]

theoretical = [
    analytical[total]
    for total in sums
]

plt.figure(figsize=(10, 5))

plt.plot(
    sums,
    monte_carlo,
    marker="o",
    label="Монте-Карло"
)

plt.plot(
    sums,
    theoretical,
    marker="s",
    label="Теоретичні значення"
)

plt.title("Ймовірності сум при киданні двох кубиків")
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.xticks(sums)
plt.grid(True)
plt.legend()

plt.show()









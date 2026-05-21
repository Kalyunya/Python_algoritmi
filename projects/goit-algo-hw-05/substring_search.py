import timeit
from pathlib import Path

# ----------------------------------
# KMP (Кнут-Морріс-Пратт)
# ----------------------------------

def compute_lps(pattern):

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < len(text):

        if pattern[j] == text[i]:

            i += 1
            j += 1

        if j == len(pattern):
            return True

        elif i < len(text) and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False


# ----------------------------------
# Рабін-Карп
# ----------------------------------

def rabin_karp(text, pattern):

    return pattern in text


# ----------------------------------
# Боєр-Мур
# ----------------------------------

def boyer_moore(text, pattern):

    bad_char = {}

    for i in range(len(pattern)):
        bad_char[pattern[i]] = i

    m = len(pattern)
    n = len(text)

    shift = 0

    while shift <= n - m:

        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            return True

        shift += max(
            1,
            j - bad_char.get(
                text[shift + j],
                -1
            )
        )

    return False


# ----------------------------------
# Завантаження текстів
# ----------------------------------

current_dir = Path(__file__).parent

article1_path = current_dir / "article1.txt"
article2_path = current_dir / "article2.txt"


with open(article1_path, encoding="utf-8") as file:
    text1 = file.read()

with open(article2_path, encoding="utf-8") as file:
    text2 = file.read()

existing = "алгоритм"
fake = "qwerty123456789"


algorithms = {
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp,
    "Boyer-Moore": boyer_moore
}


def test_text(text, text_name):

    print(f"\n{text_name}")
    print("=" * 40)

    for name, algorithm in algorithms.items():

        exist_time = timeit.timeit(
            lambda: algorithm(text, existing),
            number=10
        )

        fake_time = timeit.timeit(
            lambda: algorithm(text, fake),
            number=10
        )

        print(
            f"{name}"
            f"\nІснуючий рядок: {exist_time:.6f}"
            f"\nНеіснуючий рядок: {fake_time:.6f}\n"
        )


test_text(text1, "Стаття 1")
test_text(text2, "Стаття 2")
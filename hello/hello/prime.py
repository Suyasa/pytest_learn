from typing import List


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


# List[int] で要素が int のリスト型を表す型ヒントになる
def load_numbers_sorted(txt: str) -> List[int]:
    numbers = []

    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))

    return numbers

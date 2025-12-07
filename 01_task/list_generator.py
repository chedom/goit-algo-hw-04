import random


def generate_random_list(n: int) -> list[int]:
    return [random.randint(0, 10_000) for _ in range(n)]


def generate_sorted_list(n: int) -> list[int]:
    return list(range(n))


def generate_reverse_sorted_list(n: int) -> list[int]:
    return list(range(n, 0, -1))

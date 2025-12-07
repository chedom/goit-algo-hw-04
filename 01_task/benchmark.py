import timeit

from insertion import insertion_sort
from merge import merge_sort
from tim import tim_sort

from list_generator import (
    generate_random_list,
    generate_reverse_sorted_list,
    generate_sorted_list
)


def benchmark_algo(sort_func, lst, number):
    timer = timeit.Timer(lambda: sort_func(lst))
    return timer.timeit(number=number)


def run_benchmark():
    size = [10, 50, 100, 500, 1000, 5000, 10000]
    list_generators = [
        ("sorted", generate_sorted_list),
        ("reverse", generate_reverse_sorted_list),
        ("random", generate_random_list),
    ]
    sort_algos = [
        ("insertion", insertion_sort),
        ("merge", merge_sort),
        ("tim", tim_sort)
    ]

    for n in size:
        for gen in list_generators:
            gen_name, gen_fn = gen
            print(f"\n{n}  {gen_name.capitalize()}\n")
            lst = gen_fn(n)
            for algo in sort_algos:
                algo_name, algo_fn = algo
                # important to pass copy of the list
                res = benchmark_algo(algo_fn, lst.copy(), 100)
                print(f"Run bench for {algo_name.capitalize()}: {res}")

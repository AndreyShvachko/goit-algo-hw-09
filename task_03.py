import timeit
from task_01 import find_coins_greedy
from task_02 import find_min_coins

def measure_time ():
    amounts = [113, 999, 10000]

    for amount in amounts:
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount),  number=1000)
        dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)

        print(f"Для суми {amount}:")
        print(f"Час виконання жадібного алгоритму: {greedy_time} секунд")
        print(f"Час виконання динамічного програмування: {dp_time} секунд")
        print("-" * 50)

measure_time()


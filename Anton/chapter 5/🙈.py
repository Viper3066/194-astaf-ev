import random
import time
# Реализация сортировки слиянием
def merge_sort(arr):
    if len(arr) <= 1:  # базовый случай
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    n = m = k = 0
    c = [0] * len(arr)

    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            c[k] = left[n]
            n += 1
        else:
            c[k] = right[m]
            m += 1
        k += 1

    while n < len(left):
        c[k] = left[n]
        n += 1
        k += 1

    while m < len(right):
        c[k] = right[m]
        m += 1
        k += 1

    for i in range(len(arr)):
        arr[i] = c[i]  # здесь было исправлено присваивание

    return arr
# Реализация сортировки выбором
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Функция для генерации случайного списка заданной длины
def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]


def test():
    # Сравнение эффективности алгоритмов на случайных списках разных размеров
    for size in [100, 1000, 10000, 100000]:
        arr = generate_random_list(size)

        # Измерение времени выполнения сортировки слиянием
        start_time = time.time()
        merge_sort(arr.copy())
        merge_sort_time = time.time() - start_time

        # Измерение времени выполнения сортировки выбором
        start_time = time.time()
        selection_sort(arr.copy())
        selection_sort_time = time.time() - start_time

        print(f"Размер списка: {size}")
        print(f"Время выполнения сортировки слиянием: {merge_sort_time:.5f} сек")
        print(f"Время выполнения сортировки выбором: {selection_sort_time:.5f} сек")
        print("=" * 50)


if __name__ == "__main__":
    test()

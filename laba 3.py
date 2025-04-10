from itertools import permutations
#Вариант 12
# ЗАДАЧА 1
#без рекурсии
def k_permutations_iterative(lst, k):
    return list(permutations(lst, k))
#С рекурсией
def k_permutations_recursive(lst, k):
    if k == 0:
        return [[]]
    if not lst:
        return []
    result = []
    for i in range(len(lst)):
        current = lst[i]
        rest = lst[:i] + lst[i+1:]
        for perm in k_permutations_recursive(rest, k - 1):
            result.append([current] + perm)
    return result
lst = [1, 2, 3]
k = 2
print("ЗАДАЧА 1: Перестановки длиной", k)
print("Итеративно:", k_permutations_iterative(lst, k))
print("Рекурсивно:", k_permutations_recursive(lst, k))
# ЗАДАЧА 2
# x_i = i * x_(i-1) + 1/i, x_0 = 0
# Без рекурсии
def sequence_iterative(n):
    x = 0
    for i in range(1, n + 1):
        x = i * x + 1 / i
    return x
# С рекурсией
def sequence_recursive(n):
    if n == 0:
        return 0
    return n * sequence_recursive(n - 1) + 1 / n
n = 4
print("ЗАДАЧА 2: Вычисление x_n при n =", n)
print("Без рекурсии:", sequence_iterative(n))
print("С рекурсией:", sequence_recursive(n))
# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

n = int(input('Введите число: '))
def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))

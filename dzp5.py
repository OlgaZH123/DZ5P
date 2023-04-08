# Задача 26:Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def numbers_pow(m, n, result=1):
#     if n == 0:
#         return result
#     return numbers_pow(m, n - 1, result * m)


# def main():
#     number = int(input('Введите число, возводимое в степень: '))
#     degree = int(input('Введите требуемую степень числа: '))
#     print(numbers_pow(number, degree))


# if __name__ == '__main__':
#     main()

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def get_summ_numbers(a, b, summ_numbers=0):
    if a == 0 and b == 0:
        return summ_numbers
    elif a != 0 and b != 0:
        summ_numbers += 2
        return get_summ_numbers(a - 1 if a > 0 else 0, b - 1 if b > 0 else 0, summ_numbers)
    else:
        summ_numbers += 1
        return get_summ_numbers(a - 1 if a > 0 else 0, b - 1 if b > 0 else 0, summ_numbers)


def main():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(get_summ_numbers(a, b))


if __name__ == '__main__':
    main()
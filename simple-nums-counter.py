def is_simple(num: int):
    sqrt_num = int(num ** 0.5) + 1
    for i in range(2, sqrt_num):
        if (num % i == 0):
            return 0
    return 1


def count_simple_nums(number: int):
    if number == 1:
        return 1
    if is_simple(number):
        return number - 1

    cnt = 0
    for i in range(2, number):
        cnt += (1 if number % i else 0)
    return cnt


print(count_simple_nums(1_000_000))  # Самое последнее простое число 999951

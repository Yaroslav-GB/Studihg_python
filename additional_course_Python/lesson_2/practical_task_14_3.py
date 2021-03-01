from math import sqrt

num_list = [2, -5, 8, -6, 6, 10, 7, 9, -2, 5, 8, 4, -5, 6, 7, -4, 4, 10, 5]
print(list)


def to_pow_nums(list):
    return [round(sqrt(num), 3) if num > 0 else num for num in num_list]


print(to_pow_nums(num_list))

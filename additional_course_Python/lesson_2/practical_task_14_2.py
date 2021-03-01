from random import randint

num_list = [randint(-10, 10) for i in range(20)]

# new_fruit_list = [fruit for fruit in fruit_list_1 if fruit in fruit_list_2]

print(num_list)

multiple_list_3 = [num for num in num_list if num % 3 == 0]
positive_list = [num for num in num_list if num > 0]
multiple_list_4 = [num for num in num_list if num % 3 == 0]

print(multiple_list_3)
print(positive_list)
print(multiple_list_4)

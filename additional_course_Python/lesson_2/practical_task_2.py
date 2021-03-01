from random import randint

num_list = randint(1, 100)
print(num_list)


def to_detect_13(list):
    return [num ** 2 for num in num_list]


# try:
if to_detect_13(num_list) != pow(13):
    print(to_detect_13(num_list))
else:
    raise ValueError
# except:


print(to_detect_13(num_list))

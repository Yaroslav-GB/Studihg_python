fruit_list_1 = ['apple', 'orange', 'cherry', 'peach', 'apricot']
fruit_list_2 = ['apple', 'grapes', 'cherry', 'banana', 'strawberry']

new_fruit_list = [fruit for fruit in fruit_list_1 if fruit in fruit_list_2]

print(new_fruit_list)

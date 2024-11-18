# chastina 2 dz1
# expression = input("Введіть арифметичний вираз: ")
#
# try:
#     result = eval(expression)
#     print(f"Результат виразу: {result}")
# except Exception as e:
#     print("Помилка при обчисленні виразу:", e)

# dez2
# import random
#
# n = int(input("Введіть кількість елементів у списку: "))
# numbers = [random.randint(-100, 100) for _ in range(n)]
#
# print("Список чисел:", numbers)
#
# negative_count = 0
# positive_count = 0
# zero_count = 0
#
# min_value = min(numbers)
# max_value = max(numbers)
#
# for num in numbers:
#     if num < 0:
#         negative_count += 1
#     elif num > 0:
#         positive_count += 1
#     else:
#         zero_count += 1
#
# print(f"Мінімальний елемент: {min_value}")
# print(f"Максимальний елемент: {max_value}")
# print(f"Кількість від'ємних елементів: {negative_count}")
# print(f"Кількість додатних елементів: {positive_count}")
# print(f"Кількість нулів: {zero_count}")
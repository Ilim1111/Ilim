# 1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}. Объедините их в один при помощи встроенных функций языка Python. Подсказка: метод update()
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)
# 2) Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2, ‘num_3’ : 3, ‘num_100’ : 100} Необходимо умножить все числовые значения словаря на 5 и вывести в терминал. 
# numbers = {"num_1" : 1, "num_2" : 2, "num_3" : 3, "num_100" : 100}
# b = numbers.values()
# for i in b:
#     print(i*5)



    
# 3) Есть словарь student = {"name" : "Askhat", "age" : 17}. Умножьте его age на 2 раза 
# student = {"name" : "Askhat", "age" : 17}
# student["age"]=34
# print(student)

# # 4) Есть словарь student = {"name" : "Askhat", "age" : 17, "color" : "White"}. Обновите age в 16 и color на Black
# # student = {"name" : "Askhat", "age" : 17, "color" : "White"}
# # student["age"]=16
# # student["color"]="Black"
# # print(student)

# # 5) Есть словарь student = {"name" : "Askhat", "age" : 17}. Удалите ключ и значение age 
# # student = {"name" : "Askhat", "age" : 17}
# # del student["age"]
# # print(student)

# # 6) Есть словарь student = {"name" : "Askhat"}. Добавьте новый ключ(address) и значение(Западный Анар) 
# # student = {"name" : "Askhat"}
# # student["address"]="Западный Анар"
# # print(student)

# # 7)  Напишите программу, которая принимает словарь с именами студентов в качестве входных данных. Затем программа должна вывести на экран имена студентов, отсортированные в алфавитном порядке.
# # a = {"Islam": 20, "Nurbo": 18, "Sema": 22, "Ilim": 19}

# # b = sorted(a.keys())

# # for i in b:
# #     print(i)


# # 8)  Напишите программу, которая принимает словарь с именами и оценками студентов в качестве входных данных. Программа должна вывести имя студента с наивысшей оценкой.
# # a = {"Islam": 97, "Nurbo": 99, "Sema": 98, "Ilim": 100}
# # b = max(a.values())
# # for i, g in a.items():
# #     if g == b:
# #         print(i)
# # 9)  Напишите программу, которая объединяет два словаря, добавляя значения одинаковых ключей. Если ключ отсутствует в одном из словарей, он должен быть добавлен в результат с соответствующим значением.
# # a = {"Islam": 97, "Nurbo": 99, "Sema": 98, "Ilim": 100}
# # b = {"Islam": 97, "Nurbolot": 93, "Sema": 98, "Ilim": 100, "Ilimbek": 96}
# # for key, value in a.items():
# #         if key in b:
# #             b[key] += value
# #         else:
# #             b[key] = value
# # print(b)

# # 10)  Напишите программу, которая принимает список словарей, представляющих студентов, и выводит на экран среднюю оценку для каждого студента.


# students = [
# {
# 'name': 'Sima',
# 'grades': [85, 90, 92]
# },
# {
# 'name': 'Ilim',
# 'grades': [78, 85, 80]
# },
# {
# 'name': 'Nurbo',
# 'grades': [92, 87, 90]
# }
# ]
# for i in students:
#     a = i['grades']
#     b = sum(a) / len(a)
#     print(f"Средняя оценка студента {i['name']}: {b}")


# 11) Напишите программу, которая принимает словарь с числами в качестве входных данных. Программа должна найти ключ, у которого значение максимально близко к среднему значению всех чисел.

# def find_closest_key(dictionary):
#     if not dictionary:
#         return None

#     values = list(dictionary.values())
#     average = sum(values) / len(values)

#     closest_key = None
#     closest_difference = float('inf')

#     for key, value in dictionary.items():
#         difference = abs(value - average)
#         if difference < closest_difference:
#             closest_difference = difference
#             closest_key = key

#     return closest_key

# my_dict = {'a': 10, 'b': 5, 'c': 8, 'd': 12}
# closest_key = find_closest_key(my_dict)
# print(f"Средняя ближающая число: {closest_key}")




# 12) Напишите программу, которая принимает список словарей, представляющих продукты и их цены, и выводит на экран общую стоимость всех продуктов.


# def calculate_total_cost(products):
#     total_cost = 0

#     for product in products:
#         if 'price' in product:
#             total_cost += product['price']

#     return total_cost



# product_list = [
#     {'name': 'Product 1', 'price': 10},
#     {'name': 'Product 2', 'price': 20},
#     {'name': 'Product 3', 'price': 15}
# ]
# total_cost = calculate_total_cost(product_list)
# print(f"Суммарная стоимость всех продуктов составляет: {total_cost}")
# 13) Напишите программу, которая принимает словарь с названиями стран и их столицами в качестве входных данных. Затем программа должна позволить пользователю вводить названия стран и выводить соответствующие столицы.

# def find_capital(country_dict):
#     while True:
#         country = input("Введите название страны: ")
#         if country == 'выход':
#             break

#         capital = country_dict.get(country)
#         if capital:
#             print(f"Столица {country}: {capital}")
#         else:
#             print(f"Информация о столице страны {country} не найдена.")



# countries = {
#     'Россия': 'Москва',
#     'США': 'Вашингтон, Д.C.',
#     'Великобритания': 'Лондон',
#     'Франция': 'Париж'
# }

# find_capital(countries)


# 14)  Напишите программу, которая принимает список словарей с информацией о студентах, включая их имена, возраст и оценки. Программа должна вывести на экран имена студентов, которые получили максимальные оценки и имеют возраст больше 18 лет.


# student_list = [
#     {'name': 'Алексей', 'age': 20, 'grade': 95},
#     {'name': 'Мария', 'age': 19, 'grade': 90},
#     {'name': 'Иван', 'age': 21, 'grade': 95},
#     {'name': 'Елена', 'age': 22, 'grade': 88},
#     {'name': 'Павел', 'age': 17, 'grade': 92}
# ]

# max_grade = 0
# top_students = []

# for student in student_list:
#     if student['age'] > 18:
#         grade = student['grade']
#         if grade > max_grade:
#             max_grade = grade
#             top_students = [student['name']]
#         elif grade == max_grade:
#             top_students.append(student['name'])

# if top_students:
#     print("Имена студентов с максимальными оценками и возрастом больше 18 лет:")
#     for student_name in top_students:
#         print(student_name)
# else:
#     print("Нет студентов с максимальными оценками и возрастом больше 18 лет.")

# ДОП Задание: 

# 7) Напишите программу, которая имитирует проверку пароля, придуманного пользователем. 

# Пользователь вводит пароль, а потом ещё раз его же, для подтверждения.

# И пароль который вводит пользователь записывается в пустое множество после проверок 

# Если первый пароль, который ввел пользователь короче 8 символов, программа выводит на экран слово "Короткий пароль!" 

# Если же первый пароль достаточно длинный, но в нём содержится сочетание символов "123", программа выводит на экран слово "Простой пароль!" 

# Если же предыдущие проверки пройдены успешно, но введённые слова-пароли не совпадают, то программа выводит на экран слово "Различаются."

# Если же и третья проверка пройдена успешно, программа выводит "OK" (латинскими буквами) и выводит “Пароль создан!”


# password1 = input("Введите пароль: ")
# password2 = input("Повторите пароль: ")

# password_set = set()

# if len(password1) < 8:
#     print("Короткий пароль!")
# else:
#      password_set.add(password1)
# if "123" in password1:
#     print("Простой пароль!")
# elif password1 != password2:
#      print("Различаются.")
# else:
#      print("OK")
# print("Пароль создан!")
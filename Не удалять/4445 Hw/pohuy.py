# import random

# 1) Создайте две переменные, num1 со значением 5 и num2 со значением 10. Сложите эти переменные и выведите результат на экран.
# num1 = 5
# num2 = 10
# print(num1+num2)
#  2) Создайте две переменные, num1 со значением 10 и num2 со значением 5. Вычтите из переменной num1 переменную num2 и выведите результат на экран. 

# 3) Создайте две переменные, num1 со значением 20 и num2 со значением 5. Умножьте переменную num1 на переменную num2, а затем разделите результат на 2. Выведите полученный результат на экран. 

# 4) Создайте три переменные, x со значением 10, y со значением 5 и z со значением 2. Вычислите результат выражения (x + y) * z и выведите его на экран. 
	
# ДОП ЗАДАНИЕ: 
# 5) Создайте две переменные, num1 со значением 5 и num2 со значением 10. Сравните эти переменные с помощью операторов "<" и ">", и выведите результат на экран. Пример вывода: num1 < num2: True num1 > num2: False
# num1 = 5
# num2 = 10
# print("true",num1<num2)
# print(num1>num2)





# ЗАДАЧА №1
# Написать программу, которая будет проверять пароль. Пусть программа в начале
# запросит пароль у пользователя. В самой программе сохраните определенный пароль
# и сравните его с тем, который был введен пользователем. В случае, если пароли
# совпадают, то выведете на экран следующее сообщение: "Password is correct. You are
# welcome’ Если нет: ‘Password is incorrect. Please, try again’
# Программу решить 2 способами, 4 строчной if else конструкцией и 1 строчной версией
# if else.
# num = "ilim"
# num1 = (input("Введите пароль: "))
# if num == num1:
#     print("Password is correct. You are welcome")
# else:
#     print("Password is incorrect. Please, try again")
# ЗАДАЧА №2
# Написать программу, которая будет спрашивать у пользователя температуру за окном.
# Используя условные конструкции if elif else, напишите программу, которая выводит на
# экран следующее:
# 1) При условии меньше -30 градусов: “Там так холодно, лучше дома сиди!”
# 2) При условии от -30 до 0: “Холодновато. Оденься потеплее!”
# 3) При условии от 0 до 15: “Прохладно. Куртку накинь!”
# 4) При условии от 15 до 30: “Тепло. Иди погуляй в парке!”
# 5) При условии от 30 до 50 включительно: “Ого, как жарко!”
# 6) При условии выше 50: “Там такая жара, лучше сиди дома!”
# 7) В других случаях: “Ошибка!”
# n = int(input("Какая температура за окном: "))
# if n <= -30:
#     print("Там так холодно, лучше дома сиди!")
# elif n > -30 and n <=0:
#     print("“Холодновато. Оденься потеплее!”")
# elif n > 0 and n <= 15:
#     print("Прохладно. Куртку накинь!")
# elif n > 15 and n <= 30:
#     print("“Тепло. Иди погуляй в парке!")
# elif n > 30 and n < 50:
#     print("Ого, как жарко!")
# elif n > 50:
#     print("Там такая жара, лучше сиди дома!")
# else:
#     print("Ошибка!")
# ЗАДАЧА №3
# Вам дается текст:
# Advertising companies say advertising is necessary and important. It informs people about
# new products. Advertising hoardings in the street make our environment colourful. And
# adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
# programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
# healthy products. And adverts in magazines give us ideas for how to look prettier, be
# fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad
# for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
# know we love our children and want to give them everything. So they use children’s ‘pester
# power’ to sell their products. Finally, consumers say, if there is advertising there must be
# rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
# money.
# Посчитайте количество букв s и t .
# c ='''Advertising companies say advertising is necessary and important. It informs people about
#  new products. Advertising hoardings in the street make our environment colourful. And
#  adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
#  programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
#  healthy products. And adverts in magazines give us ideas for how to look prettier, be
#  fashionable and be successful. Without advertising, life is boring and colourless.
#  But some consumers argue that advertising is a bad thing. They say that advertising is bad
#  for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
#  know we love our children and want to give them everything. So they use children’s ‘pester
#  power’ to sell their products. Finally, consumers say, if there is advertising there must be
#  rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
#  money.
#  Посчитайте количество букв s и t .'''
# c.count("t")
# print(c.count("s"))
# print(c.count("t"))
# ДОП ЗАДАЧА:
# Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную
# строку из двух имен, буква за буквой.
# Результат: "AAiddialnea
# a = "Aidana"
# b = "Adilet"
# print(a[0] + b[0]+ a[1] + b[1]+ a[2] + b[2]+ a[3] + b[3]+a[4] + b[4]+ a[5] )




# Задача 1:
# Напишите программу, которая запрашивает у пользователя его возраст и выводит сообщение, указывающее на его категорию:
# - Если возраст меньше 18, вывести сообщение "Вы являетесь несовершеннолетним."
# - Если возраст от 18 до 65 включительно, вывести сообщение "Вы являетесь взрослым."
# - Если возраст больше 65, вывести сообщение "Вы являетесь пожилым."
# a = int(input("Введите ваш возраст: "))
# if a < 18:
#     print("Вы являетесь несовершеннолетним.")
# elif a >= 18 and a < 65:
#     print("Вы являетесь взрослым")
# elif a >= 65:
#     print("Вы являетесь пожилым.")
# else:
#     print("error")

# Задача 2:
# Напишите программу, которая запрашивает у пользователя три числа и выводит наименьшее из них.
# a = int(input("Введите 1ое "))
# b = int(input("Введите 2ое "))
# c = int(input("Введите 3ее "))
# if a < b and a < c :
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < a and c < b:
#     print(c)



# Задача 3:
# Создайте вручную список из 15 элементов (название городов, музыки, машины). Сделайте срез от 2-го индекса до 7-го 
# a = ["Experienced", "programmers", "in", "any", "other", "language", "can", "pick", "up", "Python", "very", "quickly", "and", "beginners", ]
# print(a[0:7])

# Задача 4:
# Создайте вручную список из 10 элементов (название городов, музыки, машины).Удалите из списка 2 и 8 индекс . и добавьте в список 5 новых элементов в конец списка
# a = ["Experienced", "programmers", "in", "any", "other", "language", "can", "pick", "up", "Python",]
# a.pop(2)
# a.pop(8)
# print(a)
# a.append("beginners")
# a.append("very")
# a.append("quickly")
# a.append("and")
# a.append("beginners")
# print(a)

# 	Задача 5:
# Создайте список от 0 до 20  и удалите число 2 и 16 и добавьте в начало списка число 5 и 9.
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# a.pop(1)
# a.pop(14)
# print(a)
# a.insert(0,5)
# a.insert(1,9)
# print(a)
# Задача 6:
# У вас есть список из рандомных чисел
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# Ваша задача:
# Отсортировать список numbers в порядке возрастания и вывести его.
# Используйте подходящий метод списка для сортировки и выведите отсортированный список.
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]

# numbers.sort()
# print(numbers)

# Задача 7:
# Из списка указанного в 6 задачи, переверните список после сортирования.Используйте подходящий метод списка для и выведите перевернутый и отсортированный  список.
# numbers = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 12, 12, 21, 24, 32, 32, 34, 36, 43, 43, 43, 44, 45, 45, 52, 56, 56, 58, 65, 73, 75, 98, 235, 321, 452, 653, 654, 909, 954]
# numbers.reverse()
# print(numbers)
# Задача 8:
# Из списка указанного в 6 задачи.Выясните сколько раз число 2, 5 и 3  встречается в списке.
# a = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
#  print(a.count(2))
# print(a.count(5))
# print(a.count(3))
# 	Задача 9:
# Создайте список от 1 до 20 и найдите среднее арифметическое число.
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Доп задание:
# У вас есть список numbers = [1,2,3,4,5,6,7,8,9,10,]
# Задача 1:
#  Найдите наименьший элемент в списке из доп задания.
# numbers = [1,2,3,4,5,6,7,8,9,10,]
# print(min(numbers))

# Задача 3:
#  Найдите наибольший элемент в списке из доп задания.
# print(max(numbers))
# Задача 4:
#  Найдите сумму элементов в списке из доп задания.
# print(sum(numbers))
# Задача 5:
# 9) Создайте плейлист из 10 любимых песен, поменяйте 4-й с 8-м и выведите на экран весь плейлист
# m = ["Далеко за закатами", "Музыка для души", "Как ты там-c кем ты там", "mon ami", "tgg", "за плохое-за хоршоее", "Музе", "забытый бала", "52" "герца", "Второй том",]
#     ЧТОБЫ МЕНЯТЬ МЕСТАМИ 
# m[3] , m[7] = m[7] , m[3]
# print(m)

# Задача 6:
# Создайте список от 0 до 20. и удалите из списка все четные числа и выведите результат.

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in a:
#     if i %2 ==0:
#         a.remove(i)
# print(a)
       

# 1) Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужно превратить кортеж в список и добавить новое значение ‘Tesla’, затем превращаете список обратно в кортеж 
# it_company = ("Google", "Amazon", "Microsoft")
# l= list(it_company)
# l.append("Tesla")
# print(l)

               
# 2) Из 6 задания попробуйте вывести индекс "Amazon" 
# print(it_company[1])
# 3) Из 6 задания обновите значение "Google" на "Apple" любыми способами 
# it_company[0]="Apple"
# print(it_company)
# 4) Из 6 задания сделайте выведите срез "Apple" до "Microsoft" 
# print(it_company[0:3])
# 5) Есть кортеж text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview') вам нужно посчитать сколько раз встречается слово python
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count("Python"))
# 6) Создайте кортеж из 20 элементов, удалите элементы от 3 до 9 после выведите результат используя цикл. Вместе удаленных напишите новых 5 элементов после выведите кортеж обычным образом и также циклом. 
# a = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation',)
# lister = list(a)
# lister.pop(3)
# lister.pop(4)
# lister.pop(5)
# lister.pop(6)
# lister.pop(7)
# lister.pop(8)
# for i in lister:
#     print(i)
# lister.append("1")
# lister.append("2")
# lister.append("3")
# lister.append("4")
# lister.append("5")
# for i in lister:
#     print(i)


# 7)  Нужно заполнить пустой список от 1 до 100. Полученный результат вывести на экран. Подсказка: используйте функцию range() и пустой список
# l = []
# for i in  range(1,101):
#     l.append(i)
# print(l)
# 8)  Суммирование тысячу чисел: создайте список чисел от 1 до 1 000, затем воспользуйтесь функциями min() и max() и убедитесь в том, что список действительно начинается с 1 и заканчивается 1 000. Вызовите функцию sum() и посмотрите, насколько быстро Python сможет просуммировать тысячу чисел
# l = []
# for i in range(1,1001):
#     l.append(i)
# print(l)
# print(min(l))
# print(max(l))
# print(sum(l))
# 1sek

# 9) Вывести на экран все чётные значения в диапазоне от 1 до 497. Подсказка: используйте функцию range() или условия
# l = list(range(1,497))
# for i in l :
#     if i%2==0:
#         print(i)


# 10) Создайте калькулятор который будет запрашивать у пользователя два N числа. И программа должна запрашивать шаг пользователя ( сложить, вычитание, деление, умножение), И программа должна выполнить шаг пользователя ( делить, умножить, сложить, вычесть) и должен вывести результат. Добавьте туда цикл While чтобы программа не останавливалась. 
# while True:
#     a = int(input("Введите 1ое число: "))
#     b = int(input("Введите 2ое число: "))
#     print(" сложить, вычитание, деление, умножение")
#     c = input("+, -, *, / : ")
#     if c == "+":
#         print(a+b)
#     elif c =="-":
#         print(a-b)
#     elif c =="*":
#         print(a*b)
#     elif c =="/":
#         print(a/b)
#     else:
#         print("error")

# ДОП ЗАДАНИЕ

# 1) Сделайте игру Камень, Ножницы, Бумага .Добавьте туда цикл while, также у пользователя должно быть 5 попыток и каждый раз вы должны отнимать попытки по 1. Если попытки закончятся цикл должен остоновится и программа должна вывести  текст <<Игра окончена, у вас осталось 0 попыток>>


# a = input("Камень, Ножницы, Бумага: ")
# b = ('Камень', 'Ножницы', 'Бумага')
# r = random.choice(b)
# print(r)
# if a == b:
#     print("Ничья")
# elif (a == 'Бумага' and r == 'Камень') or (a == "Камень" and r == "Ножницы") or (a == "Ножницы" and r == "Бумага"):
#     print("вы выиграли")
# else:
#     print("Вы выиграли!")




# 2)  12) Создайте бесконечный цикл. Запросите у пользователя его возраст. Если ему есть 18 лет, выведите: "Доступ разрешен" и остановите цикл, иначе "Извините, пользование данным ресурсом только с 18 лет" и запросите заново

# while True:
#     a = int(input("Введите ваш возраст: "))
#     if a >=18:
#         print("Доступ разрешен")
#         break
#     if a < 18:
#         print("Извините, пользование данным ресурсом только с 18 лет")
        
        
# 3) Напишите программу, которая считывает строку от пользователя и выводит её перевёрнутую версию. Например, если строка "Hello, World!", то программа должна вывести "!dlroW ,olleH".
# a = input('Введите чета: ')

# print(a[::-1])











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

# c = ""
# a = (input("Введите пароль: "))
# b = (input("Введите еще раз для подтверждения: "))
# if a != b:
#     print("Различаются.")
# elif len(a) <8:
#     print("Короткий пароль!")
# elif "123" in a:
#     print("Простой пароль!")
    
# else:
    
#     print("Пароль создан")












# 2,7,
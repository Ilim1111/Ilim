# 1 Задание 
# age  = int(input("Введите возраст: "))
# if  age < 18:
#     print("Вы являетесь несосершеннолетним.")
# elif age >= 18 and age <65:
#     print("Вы являетесь взрослым.")
# elif age > 65 and age <=120:
#     print("Вы являетесь пожилым.")
#     # это типа доп
# elif age >= 121:
#     print("Вы походу бессмертный😂🤙.")

# 2 Задание
# num1 = int(input("Введите число:  "))
# num2 = int(input("Введите число:  "))
# num3 = int(input("Введите число:  "))

# if num1 < num2 and num1 <num3:
#     print(f"{num1} - самая маленькая")
# elif num2 <num1 and num2 <num3:
#     print(f"{num2} - самая маленькая,")
# elif num3 <num1 and num3 <num2:
#     print(f"{num3} - самая маленькая.")  
# else:
#     print(".") 

# 3 Задание
# lister = ["Osh", "Honda", "Semerka", "Ihone", "Bishkek", "Geeks", "Aravanskaya", "Zapad", 'Vostok', 'Batken', 'Talas', 'Tesla', 'BMW', 'Eki Dos', 'KFC' ]
# print(lister[2:7])

# 4 Задание 
# name = ["Osh", "Honda", "Semerka", "Ihone", "Bishkek", "Geeks", "Aravanskaya", "Zapad", 'Vostok', 'Batken']
# name.pop(2)
# name.pop(7)
# print(name) 
# name.append("Water")
# name.append("Apple")
# name.append("Laptop")
# name.append("Orangre")
# name.append("Potato")
# print(name)

# 5
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# numbers.pop(1)
# numbers.pop(14)
# print(numbers)
# numbers.insert(0,(5))
# numbers.insert(1,(9))
# print(numbers)

# 6
# numbers1 = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# numbers1.sort()
# print(numbers1)
# # 7
# numbers1 = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# numbers1.sort()
# numbers1.reverse()
# print(numbers1)

# 8 
# num5 = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# print("Здесь",num5.count(2)," "+"(2)")
# print("Здесь",num5.count(5)," "+"(5)")
# print("Здесь",num5.count(3)," "+"(3)")

# 9
# num6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(sum(num6) / len(num6))

# Доп Задание 1
# num7 =  [1,2,3,4,5,6,7,8,9,10,]
# print(min(num7))

# Доп 3
# num7 =  [1,2,3,4,5,6,7,8,9,10,]
# print(max(num7))

# доп 4
# num7 =  [1,2,3,4,5,6,7,8,9,10]
# print(sum(num7))

# Доп 5
# musics = ["Далеко за закатами", "Музыка для души", "Как ты там-c кем ты там", "mon ami", "tgg", "за плохое-за хоршоее", "Музе", "забытый бала", "52" "герца", "Второй том",]
# musics[3],musics[7] = musics[7],musics[3]
# print(musics)

# # доп 6
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in list:
#     if i % 2 == 0:
#         list.remove(i)
# print(list)
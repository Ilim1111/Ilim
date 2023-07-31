# def name():
#     print("Hello World")
# user = input("Введите свое имя: ")
# name()


# Пример 1
# name = lambda: print("Hello World")
# name()

# number = [4,2,5,1,5]
# for i in number:
    
#     print(i*2) 

# my_list = [4,2,5,1,5]
# def number(numbe):
#     for num in numbe:
#         print(num*2)
# number(numbers)

# Пример 2

# lambda_numbers = list(map(lambda numbers:numbers*2,my_list))
# print(lambda_numbers)

# Пример 3

# def multiply(x,y):
#     print(x*y)
# multiply(1,8)

# multiply = lambda x,y: x*y
# print(multiply(6,9))

# Пример 4

# n = lambda x,y: [x+y ,x-y , x*y , x/y]
# print(n(456,72))

#  Работа с файлами
# пример 1
# text = open('lesson.txt','w') # w - write
# text.write('print(5+5)')
# text.close

# пример 2


# text = open('ilim.txt','r')
# result = text.read()
# print(result)

# пример 3

# with open('geeks.txt', 'w') as text:
    # text.write('Hello Geeks')

# пример 4
with open ('ilim.txt','r') as text:
    content = text.read()
    print(content)
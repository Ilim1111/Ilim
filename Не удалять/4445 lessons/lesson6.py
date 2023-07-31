# Функции
# Встроеные функции
# print ("Hello World")

# 2 Не встроеные функции

# def geeks():
#     b = 2 + 2
#     print(b)

# geeks()

# def g():
#     b = "Hello Ilim how are you"
#     print(b)

# g() 

# def i():
#     print("Hello Ilim how are you")

# i()

# def welcome():
#     name = input("Введите свое имя: ")
#     print(f"Добро пожаловать {name}")
# welcome()

# def calculator():
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
  
#     c = input("Выберите +, -, *, / : ")
#     if c == "+":
#         print(a+b)
#     elif c == "-":
#         print(a-b)
#     elif c == "*":
#         print(a*b)
#     elif c == "/":
#         print(a/b)
#     else:
#         print("Не правильно сделали +, -, *, /")
# calculator()

# def Welcome(name, surname):
#     print(f"Hello {name} {surname}")

# Welcome("Ilim", "Berdiev")

# def calculator(num1 , num2):
#     print(num1+num2)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# calculator(a,b) 
# print("Hell") 


def calculator(n1 , n2 , n3):

    if n3 == "+":
        print(n2+n1)
    elif n3 == "-":
        print(n2-n1)
    elif n3 == "*":
         print(n2*n1)
    elif n3 == "/":
        print(n2/n1)
    else:
        print("Не правильно сделали +, -, *, /")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

c = input("Выберите +, -, *, / : ")
  
calculator(a,b,c)

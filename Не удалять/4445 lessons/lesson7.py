# try , except
# args, kwargs

# def name(num1, num2):
#     try: 
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("На 0 делить нельзя")
# name(100,0)

# def calculator(n1,n2,a):
#     try:
#         if a =="+":
#             print(n1+n2)
#         elif a == "-":
#             print(n1-n2)
#         elif a == "*":
#             print(n1*n2)
#         elif a == "/":
#             try:
#                 print(n1/n2)
#             except ZeroDivisionError:
#                print("на 0 делить нельзя")
#         else:
#             print("error")
#     except TypeError:
#             print("Буквы вводить нельзя!")
# try:
#     q = int(input("Введите 1 число: "))
# except ValueError:
#     print("Буквы вводить нельзя!")
# try:
#     w = int(input("Введите 2 число: "))
# except ValueError:
#     print("Буквы вводить нельзя!")

# e = (input("+, -, *, или /: "))
# calculator(q,w,e)

# def lister(obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10):
#     list1 = []
#     list1.append(obj1)
#     list1.append(obj2)
#     list1.append(obj3)
#     list1.append(obj4)
#     list1.append(obj5)
#     list1.append(obj6)
#     list1.append(obj7)
#     list1.append(obj8)
#     list1.append(obj9)
#     list1.append(obj10)
#     print(list1)
# lister("ilim","limo","ili","mili","bee","eki","kot","queare","was","eyes")

# **
# def lister(*name):
#     list1 = []
#     for result in name:
#         list1.append(result)
#     print(list1)
# lister("ilim","limo","ili","mili","bee","eki","kot","queare","was","eyes")

# def pizza(*ing):
#     for result in ing:
#         print(f"Вы добавили в пиццу {result}.")

# pizza("Тесто","Cola","Fanta","Cheese","Fish","Sausage")

def make_pizza(**kwargs):
    for key, value  in kwargs.items():
        print(f" Размер - {value}. Адрес: {value}")
make_pizza(size = "Большой" , adress = "Geeks")

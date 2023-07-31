# number = [2,3,4,5,6,77,2,1,3,4,2]

# sum_number = 0

# for num in number:
#     sum_number += num

# print(f"Сумма чисел: {sum_number}")      


# numbers = []
# for num in range(1,45):
#     numbers.append(num)

# print(numbers)


# Множества set, frozenset

#str
# int
# float
# list
# tuple
# bool 

# a = [1,2,3,4,5]
# b = [3,4,5,6,7]
# print(a+b)
# print(set(a+b))

# st = {'Geeks', 'Osh', 'Bishkek', 'IT', 'Osh'}
# print(st)
# print(st[0]NO work

# email= {"nurbolot@gmail.com"}
# print(email)

# email.add('geeks@gmail.com')
# print(email)

# email.add("osh@gmail.com")
# print(email)

# email.add('Osh@gmail.com')
# print(email)

# email.add('geeks@gmail.com')
# print(email)

# email.add(1)
# print(email)

# email.add("1")
# print(email)

# email.remove("geeks@gmail.com")
# print(email)

# email.remove(1)
# email.remove("1")
# print(email)

# email.pop()
# print(email) 

# frozenset
frst = frozenset({1,2,3,1,2,3,4,5,6})
print(frst)


# Dictionary - словарь

# User = {'name':"Nurbolot", "surname":"Erkinbaev" ,'age':18}
# print(User)
# print(User["name"])
# print(User["age"])
# # добавить
# User["car"] = "BMW"
# print(User)
# print(User["car"])
# # print(User[0])
# # изменить
# User["name"] = "Bekbolot"
# print(User)
# # улалить
# User.pop("age")
# print(User)

# Апгрейт 
name = {"name": "nurbolot"}
surname ={"surname": "Erkinbaev"}
name.update(surname)
print(name)


keys = name.keys()
print(keys)
values = name.values()
print(values)
items = name.items()
print(items)

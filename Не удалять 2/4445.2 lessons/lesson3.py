# class Myclass():
#     def __init__(self, name, ):
#         self.name = name 
    
#     def __str__(self):
#         return f"My name is {self.name}"

# myclass = Myclass("Ilim")
# print(myclass)

# Создайте новый класс Sum и он принимает 2 аргумента name и age 
# и создайте метод который будет умножать возраст пользователя на 2
# и после выводит результат с помощью магического метода str
# class Summ():
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age

#     def double_age(self):
#         self.age *= 2

#     def __str__(self):
#         return f"Возраст {self.name} умноженая на 2 {self.age}"
# mus = Summ("Ilim", 19)
# print(mus)
# mus.double_age()
# print(mus)

# class Car():
#     def __init__(self, model , year):
#         self.model = model
#         self.year = year
    
#     def start(self):
#         print(f"{self.model}-Запушен!")
    
#     def stop(self):
#         print(f"{self.model}-Остановлен!")

# car = Car("BABAN",2015)


# class ElectroCar(Car):
#     def __init__(self, model, year):
#         super().__init__(model,year)
    
#     def change(self):
#         print(f"{self.model} заряжается!")
    
#     def change_finish(self):
#         print(f"{self.model} Зарядился!")

# electroCar = ElectroCar("BABAN",2015)
# electroCar.start()
# electroCar.stop()
# electroCar.change()
# electroCar.change_finish()

class Parent1:
    def __init__(self):
        print("Конструктор: Parent1")

    def metod_perent1(self):
        print("Я папа")

class Parent2:
    def __init__(self):
        print("Конструктор: Parent2")

    def metod_perent2(self):
        print("Я мама")

class Child(Parent1,Parent2):
    def __init__(self):
        print("Конструктор:Child")
    
    def metod_child(self):
        print("Я сын папы и мамы")

par = Parent1()
child = Child()

child.metod_perent1()
child.metod_perent2()
child.metod_child()

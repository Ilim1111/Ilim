# class Geeks:
#     def sumn(num1 , num2):
#         return num1 + num2
    


# geeks = Geeks()
# print(geeks.sumn(5,2))


# Создайте класс Nurbolot у которого будет 3 метода один должен вывести результат после вычитания,
#  второй метод умножение и третий после деления, после создайте экземпляр класса и выведите все 3 функции
# class Nurbolot:
#     def nur(num1 , num2):
#         return num1 - num2
    
#     def delen(num1, num2):
#         return num1 / num2
    
#     def um(num1 , num2):
#         return num1 * num2

# nurbolot = Nurbolot
# print(Nurbolot.nur(5,5))
# print(Nurbolot.delen(5,5))
# print(Nurbolot.um(5,5))

# class Geeks:
#     pass


class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group


        print(f"Здраствуйте {self.name} {self.surname}. Ваша группа {self.group}")


student = Student("Ilim", "Berdiev", "10")

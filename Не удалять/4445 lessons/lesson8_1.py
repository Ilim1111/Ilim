#  Первый вид импорта  Импортирование файла
# import lesson8       
# lesson8.number([12,3,4,5,6,7])


#  2 Вид импорта  Детальное импортирование
from lesson8 import number
# number([1,2,3,4,5])

# 3 вид импорта   Импортирование всего содержимого
from lesson8 import *
number([1,2,3,4,5])
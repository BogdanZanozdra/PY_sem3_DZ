#  3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.21] => 0.19

from ast import parse


numbers = [1.3, 1.25, 3.52, 10.2]
res = []
for i in numbers:
    i = str(i)
    s = i.split('.')
    print(s)
    s[0] = '0'
    s = float('.'.join(s))
    res.append(s)
print(res)    
print (f'Разница между максимальным и минимальным значением дробной части элементов: {max(res) - min(res)}')

# Или: 

array = [1.1, 1.2, 3.1, 10.01]
for i in range(len(array)):
    array[i] = round(array[i] % 1, 2)
print(max(array) - min(array))











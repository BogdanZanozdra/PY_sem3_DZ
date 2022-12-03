# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 4, 8, 5, 3, 1, 8]

def mult_pairs(listt):
    res = []
    last_index = len(listt) - 1
    if len(listt) % 2 != 0:
        for i in range(len(listt) // 2 + 1):
            res.append(listt[i] * listt[last_index])
            last_index -= 1
        return res
    else:
        for i in range(len(listt) // 2):
            res.append(listt[i] * listt[last_index])
            last_index -= 1
        return res

print(f'Произведения пар чисел списка: {mult_pairs(my_list)}')


# Или:


array = [2, 3, 4, 5, 6]
res_array = []
if len(array) % 2 == 0:
    for i in range(len(array) // 2):
        product = array[i] * array[-1-i]
        res_array.append(product)
if len(array) % 2 != 0:
     for i in range((len(array) // 2) + 1):
        product = array[i] * array[-1-i]
        res_array.append(product)

print(res_array)




















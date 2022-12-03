# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
from typing import List

n = int(input('Задайте число ряда Фибоначчи: \n'))

def fibonachi(n): 
  fib1 = fib2 = 1
  fib_list = [1, 1]
  for i in range(2, n):
      fib1, fib2 = fib2, fib1 + fib2
      fib_list.append(fib2)
  return fib_list

def negative_fib(neg_list):
  temp = neg_list.copy()
  neg_list.reverse()
  neg_list.append(0)
  neg_list = neg_list + temp
  i = 0
  while i  <= n:
    neg_list[i] *= -1
    i += 2
  return neg_list

print(fibonachi(n))
print(negative_fib(fibonachi(n)))




















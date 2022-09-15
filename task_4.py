# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите число для преобразовывания: \n"))
def bin(n):
  b = '' 
  while n > 0:
      b = str(n % 2) + b
      n = n // 2
  return b
print(f'Число {n} в десятичном виде = {bin(n)}')
print('Hello world!')

a = int(input('Введите число'))

def func(a):
  if a > 100:
    print('Огромное число!')
  elif a >= 10:
    print('Среднее число!')
  else:
    print('Небольшое число!')
    
a = 40
b = 4

if (a // b) - (b + b) == 2:
  print('Правильный ответ!')

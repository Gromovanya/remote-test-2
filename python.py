print('Hello world!')

a = int(input('Введите число'))

def func(a):
  if a > 100:
    print('Огромное число!')
  elif a >= 10:
    print('Среднее число!')
  else:
    print('Небольшое число!')
    
a = 2
b = 5

if (a * b) + (b - a)  == 13:
  print('Правильный ответ!')

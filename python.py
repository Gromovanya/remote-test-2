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
b = 3

if a + b == 5:
  print('Правильный ответ!')

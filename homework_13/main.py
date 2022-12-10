# 1. Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу
# int або float
# 2. Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки обʼєкти
# класу Point
# 3. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку
# даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника. Для обчислень можна використати формулу
# Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)


import library


point1 = library.Point(0, 0)
point2 = library.Point(3, 4)
point3 = library.Point(-10, -10)
point4 = library.Point(20, 15)
point5 = library.Point(20, -15)

my_line = library.Line(point1, point2)
my_triangle = library.Triangle(point1, point2, point3)
my_triangle2 = library.Triangle(point1, point4, point5)


print("Triangle area:", my_triangle.area())
print("Triangle 2 area:", my_triangle2.area())

print(my_triangle != my_triangle2)
print(my_triangle <= my_triangle2)
print(str(my_triangle2))

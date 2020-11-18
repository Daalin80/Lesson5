def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    s = round(0.5 * a * h, 2)
    print("Площадь треугольника: ", s)

def square():
    a = float(input("Длина стороны: "))
    s = round(a ** 2, 2)
    print("Площадь квадрата: ", s)

figure = input("""Для площади треугольника нажмите 1
Для площади квадрата нажмите 2: """)
if figure == '1':
    triangle()
elif figure == '2':
    square()
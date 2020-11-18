a = int(input("Введите сторону квадрата: "))
def square(a):
    p = round(4 * a, 2)
    s = round(a * a, 2)
    d = round(a * 2 ** 0.5, 2)
    korteg = p, s, d
    return korteg
print("Получаем периметр, площадь и диагональ: ", square(a))